class HTMLGen:

    def a(self, strng):
          return "<a>{}</a>".format(strng)

    def p(self,strng):
          return "<p>{}</p>".format(strng)

    def b(self,strng):
          return "<b>{}</b>".format(strng)

    def body(self,strng):
          return "<body>{}</body>".format(strng)

    def div(self,strng):
          return "<div>{}</div>".format(strng)

    def span(self,strng):
          return "<span>{}</span>".format(strng)

    def title(self,strng):
          return "<title>{}</title>".format(strng)

    def comment(self,strng):
          return "<!--{}-->".format(strng)