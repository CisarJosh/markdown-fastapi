import re

# TODO Create a Tokenizer class

class Markdown:
    
    heading_pattern = re.compile(r' {0,3}(#{1,6})(?:\n|\s+?(.*?)(?:\n|\s+?#+\s*?$))')
    text_pattern = re.compile(r' {0,3}(=|-)+ *$')
    link_pattern = re.compile(r'\[([^\[]+)]\(\s*(http[s]?://.+)\s*\)')
    size = 0

    @classmethod
    def heading_line(self, line: str) -> str:
        
        match = self.heading_pattern.match(line)
        if match is not None:

            self.size = len(match.group(1))
            self.content = (match.group(2) or '').strip()
            if set(self.content) == {'#'}:
                self.content = ''
            return f'<h{self.size}>{self.content}</h{self.size}>'

    @classmethod
    def linkfinder(self, line: str) -> str:
        name_regex = "[^]]+"
        url_regex = "http[s]?://[^)]+"
        markup_regex = f'\[({name_regex})]\(\s*({url_regex})\s*\)'

        for match in re.findall(markup_regex, line):
            html_link = f'<a href="{match[1]}">{match[0]}</a>'

            new_line = re.sub(f'\[({match[0]})]\(\s*({match[1]})\s*\)', html_link, line) 
            line = new_line
        return line

    @classmethod
    def paragraph(self, line: str) -> str:
        if line != '':
            return f'<p>{line}</p>'

    @classmethod
    def render_html(self, doc: str) -> str:
        """
        Render HTML from Markdown input string
        :param doc: Markdown Content String to process. 
        Capable of processing headers, paragraphs, links inline, ignoring blank lines.
        :returns: HTML String
        """
        line_number = 1
        hashmap = {}
        for line in doc.splitlines(True):
            if "\n" not in line:
                line = line + '\n'
            if line.split() == [] or line == '':
                pass
            line = self.linkfinder(line)
            if Markdown.heading_line(line):
                hashmap[line_number] = Markdown.heading_line(line)
            else:
                hashmap[line_number] = Markdown.paragraph(line)
            line_number += 1
        html = [hashmap[line] for line in hashmap]
        return "".join(html)
            


markdown = Markdown()
