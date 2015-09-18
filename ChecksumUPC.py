# import sublime
import sublime_plugin


class AddChecksumCommand(sublime_plugin.TextCommand):

    def get_checksum(self, upc):
        """Produces a checksum from an 11-digit UPC-A"""

        s = 0
        upc = iter(upc)
        for ch in upc:
            try:
                odd = int(ch)
                s += odd * 3
                even = int(next(upc))
                s += even
            except StopIteration:
                break

        return str((10 - (s % 10)) % 10)

    def run(self, edit):
        selections = self.view.sel()
        for region in selections:
            upc = self.view.substr(region)
            checkdigit = self.get_checksum(upc)
            self.view.replace(edit, region, upc+checkdigit)
