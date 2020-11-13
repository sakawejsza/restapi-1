import requests
import json
from flask import Flask, jsonify, escape, request, Response
host = '34.70.254.94' #this host needs to be updated to our correct IP address
errors = 0
import click


@click.group()
def cli():
    pass
	
	
@cli.command()
@click.option('--phrase', default= 'hello',
              help= 'The phrase to translate to md5')
def md5(phrase):
	"""This will translate a given phrase to md5"""
	t = requests.get(f'http://34.70.254.94/md5/phrase')
	print t
	pass
#####


@cli.command()
@click.option('--number', default= 1,
              help= 'The number to find factorials of')
def factorial(number):
	"""This will calcuate the factorial of a number"""
	pass
#######



@cli.command()
@click.option('--number', default= 1,
              help= 'The number to find fibonacci sequence of')
def fibonacci(number):
	"""This will return the fibonacci sequence of a number"""
	pass
#######


@cli.command()
@click.option('--number', default= 1,
              help= 'The number to be checked if prime')
def is_prime(number):
	"""This will tell you if a given number is prime or not"""
	pass
#####



@cli.command()
@click.option('--message', default= '1',
              help= 'The message to send in slack')
def slack_alert(message):
	"""This will send a slack alert and tell you if it sent sucessfully"""
	pass
#####



@cli.command()
@click.option('--post', default= '',
              help= 'post test')
def post(post):
	"""Insert a single entry into the database"""
	pass
####



@cli.command()
@click.option('--get', default= '',
              help= 'get test')
def get(user_key):
	"""Returns the entry associated with the key"""
	pass
#####



@cli.command()
@click.option('--put', default= '',
              help= 'put test')
def put(put):
	"""Updates the entry associated with the key with the value provided"""
	pass
#####



@cli.command()
@click.option('--delete', default= '',
              help= 'delete test')
def delete(user_key):
	"""Remove the entries associate with the keys provided."""
	pass
######

 
if __name__ == '__main__':
   cli()
