from formatter.tags import Tags

class TagsIndicator(Tags):
    def format(self, tags, task):
        if not tags:
            return self.markup_none(self.colorizer.tag_none())
        else:
            return (1, (self.colorizer.tag(''), self.defaults.indicator_tag))
