#HTML code to be outputted goes here in comments
class Page(object):
    def __init__(self):
        self.title = 'Food Cost Calculator'
        #add in the css
        self.css = 'http://www.teamsaner.com/RMO/main.css'
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Food Cost Calculator</title>


        <link href="http://www.teamsaner.com/RMO/main.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        '''
        self.body = '''<div class="container">

    	<h1>Weekly Food Cost Calculator</h1>
        <p>Click on a users name to reveal their weekly expenses.</p>
    <div class="chart">
		<form action="" method="GET" name="expenses" id="user-spending">
        	<input type="submit" value="Robert" name="process" class="button"><br>
            <input type="submit" value="Mary" name="process" class="button"><br>
			<input type="submit" value="James" name="process" class="button"><br>
			<input type="submit" value="Katy" name="process" class="button"><br>
			<input type="submit" value="Steve" name="process" class="button">
        </form>
     </div><!-- chart -->

    <div class="receipt">
    	<img src="receipt.jpg">
        <div class="total"></div>
    </div>
</div>
        '''
        self.close ='''
    </body>
</html>
        '''

    #function to print out the HTML code
    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
