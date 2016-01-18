from flask import session
import config
import logging

def getUser():
	if 'google_token' in session:
		googleUser = config.google.get('userinfo').data
		user = {'name': googleUser.get('name'), 'picture': googleUser.get('picture')}
		return user
	elif 'github_token' in session:
		githubUser = config.github.get( '?access_token=' + str(session['github_token'][0]) ).data
		user = {'name': githubUser.get('name'), 'picture': githubUser.get('avatar_url')}
		return user
	else:
		return None
