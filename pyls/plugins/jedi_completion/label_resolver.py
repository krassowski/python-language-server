# Copyright 2021 Michal Krassowski
from collections import defaultdict
from time import time

from jedi.api.classes import Completion

from .logger import log


class LabelResolver:

    def __init__(self, format_label, time_to_live=60 * 30):
        self.format_label = format_label
        self._cache = {}
        self._time_to_live = time_to_live
        self._cache_ttl = defaultdict(set)
        self._clear_every = 2
        # see https://github.com/davidhalter/jedi/blob/master/jedi/inference/helpers.py#L194-L202
        self._cached_modules = {'pandas', 'numpy', 'tensorflow', 'matplotlib'}

    def clear_outdated(self):
        now = self.time_key()
        to_clear = [
            timestamp
            for timestamp in self._cache_ttl
            if timestamp < now
        ]
        for time_key in to_clear:
            for key in self._cache_ttl[time_key]:
                del self._cache[key]
            del self._cache_ttl[time_key]

    def time_key(self):
        return int(time() / self._time_to_live)

    def get_or_create(self, completion: Completion):
        if not completion.full_name:
            use_cache = False
        else:
            module_parts = completion.full_name.split('.')
            use_cache = module_parts and module_parts[0] in self._cached_modules

        if use_cache:
            key = self._create_completion_id(completion)
            if key not in self._cache:
                if self.time_key() % self._clear_every == 0:
                    self.clear_outdated()

                self._cache[key] = self.resolve_label(completion)
                self._cache_ttl[self.time_key()].add(key)
            return self._cache[key]

        return self.resolve_label(completion)

    def _create_completion_id(self, completion: Completion):
        return (
            completion.full_name, completion.module_path,
            completion.line, completion.column,
            self.time_key()
        )

    def resolve_label(self, completion):
        try:
            sig = completion.get_signatures()
            return self.format_label(completion, sig)
        except Exception as e:  # pylint: disable=broad-except
            log.warning(
                'Something went wrong when resolving label for {completion}: {e}',
                completion=completion, e=e
            )
