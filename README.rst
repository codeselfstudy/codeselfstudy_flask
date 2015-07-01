CodeSelfStudy.com
=================

This is the CodeSelfStudy.com website rebuilt in Flask with Python 3. More info will be posted here soon.

Branches
--------

- :code:`master` -- don't use the master branch.
- :code:`dev` -- you can edit the dev branch, but don't upload breaking changes.

You can fork this repo and edit the `dev` branch. When ready to merge back into this repo, create a pull request. If unsure what to do, just ask. :)

Structure
---------

1. app -- contains all of the application code
2. docs -- contains any documentation that we generate
3. sandbox -- contains any code snippets and experiments that people want to share with the team, without adding that code to the actual application

Technologies
------------

Some of the proposed technologies are:

- Flask
- MongoDB with MongoEngine
- Login with password, Github, or Twitter. (add more later for practice?)
- Frontend: Bootstrap, jQuery, and Knockout.js

Resources
---------

- `Flask Quickstart <http://flask.pocoo.org/docs/0.10/quickstart/>`_ -- a quick overview to Flask.
- `Flask example <https://github.com/CodeSelfStudy/Asteroid-API-Example>`_ -- a quick example application in Flask.
- `Restructured Text Cheatsheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_ -- This is a quick cheat sheet to help with formatting .rst documents.

Coding Styles
-------------

To keep editor config sane, let's try to use the same coding style. Proposed formats are below. Discuss in chatroom or forum if you have other ideas about how things should be.

Python:

- Code should conform to PEP8 (an easy standard to follow).
- Use single quotes, in general, except where double quotes would avoid escaping the single quotes.
- Variable names and file names are snake_case.

JavaScript:

- Please use 4-space indentation (no tabs). Same as for the Python code. It's easier to skim.
- Functions should have a space between closing parenthesis and opening curly brace: :code:`function doSomething(n) { ... }`
- Anonymous functions get a space before the parentheses (the function has no name): :code:`function (e) { ... }`
- Camel case for variable names.
- CSS IDs are camelCase: :code:`$('#someId')`
- CSS classes are lowercase and have dashes: :code:`$('.some-class')`
- Curly braces should be used, even when optional.
- Semicolons should be used.
- Lines shouldn't begin with commas.
- More info here: http://codeselfstudy.com/wiki/JavaScript_Coding_Style

Licenses
--------

The loader.gif is from loading.io. The terms of use when downloaded on July 1, 2015 are: "Term of Use
All materials used in generating animated icons in this website, except the g0v icon, are created by loading.io. You can use them freely for any purpose."

DO NOT ADD COPYRIGHTED CODE TO THIS REPOSITORY. BY COMMITING CODE TO THIS REPOSITORY, YOU CERTIFY THAT THE CODE THAT YOU SUBMIT IS YOUR OWN AND THAT YOU RELEASE YOUR CONTRIBUTIONS UNDER THE PROJECT'S MIT LICENSE.
