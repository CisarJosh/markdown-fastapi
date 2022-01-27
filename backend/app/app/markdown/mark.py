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
    def linkfinder(self, token: str) -> str:
        match = self.link_pattern.match(token)
        if match:
            return f'<a href="{match.group(2)}">{match.group(1)}</a>'
    @classmethod
    def paragraph(self, line: str) -> str:
        if line != '':
            return f'<p>{line}</p>'
    @classmethod
    def render_html(self, doc: str) -> str:
        line_number = 1
        hashmap = {}
        for line in doc.splitlines(True):
            if "\n" not in line:
                line = line + '\n'
            if line.split() == [] or line == '':
                pass
            link = re.findall(r'\[([^\[]+)]\(\s*(http[s]?://.+)\s*\)', line)
            if len(link) > 1:
                pass
                # Convert to working link replacement for multiple links
                # for l in link:
                #     html_link = f'<a href="{link[0][1]}">{link[0][0]}</a>'
                #     new_line = re.sub(r'\[([^\[]+)]\(\s*(http[s]?://.+)\s*\)', html_link, line )
                #     line = new_line
            elif link:
                html_link = f'<a href="{link[0][1]}">{link[0][0]}</a>'
                new_line = re.sub(r'\[([^\[]+)]\(\s*(http[s]?://.+)\s*\)', html_link, line )
                line = new_line
                if Markdown.heading_line(line):
                    hashmap[line_number] = Markdown.heading_line(line)
                else:
                    hashmap[line_number] = Markdown.paragraph(line)
            else:
                if Markdown.heading_line(line):
                    hashmap[line_number] = Markdown.heading_line(line)
                    
                else:
                    hashmap[line_number] = Markdown.paragraph(line)
            line_number += 1
        html = [hashmap[line] for line in hashmap]
        return "".join(html)
            


markdown = Markdown()

        
    
    