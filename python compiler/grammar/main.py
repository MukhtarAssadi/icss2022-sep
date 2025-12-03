from antlr4 import *
from CommandLexer import CommandLexer
from CommandParser import CommandParser

def run_command(text):
    # Turn input into a stream
    stream = InputStream(text)

    # Lexer → tokens → parser
    lexer = CommandLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = CommandParser(tokens)

    # Start rule (your grammar entry point)
    tree = parser.command()

    print(tree.toStringTree(recog=parser))

    walker = ParseTreeWalker()
    # run_command("play cheap cards")