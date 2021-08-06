import os
import requests
from dotenv import load_dotenv
import click

load_dotenv()

subscription_key = os.environ.get('COMPUTER_VISION_SUBSCRIPTION_KEY')
endpoint = os.environ.get('COMPUTER_VISION_ENDPOINT') + "/vision/v3.1/analyze"

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = {
    'visualFeatures': 'Categories,Description,Color,adult',
    'language': 'en',
}


@click.group()
def cli():
    pass


@cli.command()
@click.option('--analyze', default="https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data"
                                   "-files/master/ComputerVision/Images/objects.jpg", type=click.STRING, help='This '
                                                                                                              'is '
                                                                                                              'will '
                                                                                                              'be '
                                                                                                              'remote '
                                                                                                              'URL to '
                                                                                                              'the '
                                                                                                              'image('
                                                                                                              'e.g '
                                                                                                              'https://example.com/hey.png)')
def run(analyze):
    """Run Image analysis."""
    try:
        body = {
            'url': analyze
        }
        response = requests.post(endpoint, headers=headers, params=params, json=body)
        response.raise_for_status()
        
        
        descriptions = response.json()["description"]["captions"]
        for description in descriptions:
            output = description['text']
            click.echo("What is happening: %s" % output)

        colors = response.json()["color"]["dominantColors"]
        output_colors = str(colors)[1:-1]
        click.echo("What colours do you see: %s" % output_colors)

        describe = response.json()["description"]["tags"]
        output_describe = str(describe)[1:-1]
        click.echo("Content in the picture: %s" % output_describe)

        adult = response.json()["adult"]["isAdultContent"]
        click.echo("Is adult content: %s" % adult)

        isGory = response.json()["adult"]["isGoryContent"]
        click.echo("Is gory content: %s" % isGory)

    except Exception as ex:
        raise ex
