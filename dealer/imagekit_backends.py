from imagekit.cachefiles.backends import CacheFileState, Simple


class SafeSimple(Simple):
    def generate_now(self, file, force=False):
        try:
            super().generate_now(file, force=force)
        except FileNotFoundError:
            self.set_state(file, CacheFileState.DOES_NOT_EXIST)
