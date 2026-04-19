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

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if not self.value:
            raise ValueError('text is missing')
        
        if not self.tag:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('tag is missing')
        
        if not self.children:
            raise ValueError('no child tag found')
        
        string = ''

        for child in self.children:
            string += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{string}</{self.tag}>'