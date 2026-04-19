class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self): # child classes will override to render themselves as Html
        raise NotImplementedError 
    
    def props_to_html(self):
        if not self.props:
            return ''
        string = ''

        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'

        return string
    
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    