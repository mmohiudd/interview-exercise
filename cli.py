import click
import picsum
import forismatic

@click.command()
@click.option('--key', '-k', 
              type=click.IntRange(1, 999999, clamp=True), 
              default=1, 
              help='Numeric key, which influences the choice of \
                quotation, the maximum length is 6 characters')

@click.option('--grayscale', '-g', 
              is_flag=True, 
              show_default=True, 
              default=False,
              help='Will fetch a grayscale image')

def cli(key, grayscale):
    """
    Fetch a random quote from the forismatic API.
    Fetch a random picture from the picsum API.
    """
    quote_text = forismatic.get_quote(key)
    
    if quote_text is None:
        quote_text = "Sorry - forismatic API is not available"

    picture = picsum.get_picture(grayscale, cli=True)

    if picture is None:
        quote_text = "Sorry - picsum API is not available"

    print(quote_text)
    print(picture)

if __name__ == '__main__':
    cli()

