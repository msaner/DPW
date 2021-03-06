#HTML code to be outputted goes here in comments
class Page(object):
    def __init__(self):
        self.title = 'Food Cost Calculator'
        #add in the css
        self.css = 'css/main.css'
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{self.title}</title>


        <link href="{self.css}" rel="stylesheet" type="text/css">
    </head>
    <body>
        '''
        self.body = '''<div class="container">

    	<h1>Weekly Food Cost Calculator</h1>
        <p>Click on a users name to reveal their weekly expenses.</p>
    <div class="chart">
        <table class="spending-chart" cellpadding="0" cellspacing="1">
        <tr>
            <td class="light"><img src="http://www.teamsaner.com/RMO/user.png" alt="user icon">
                <p>User</p>
            </td>
            <td class="dark"><img src="http://www.teamsaner.com/RMO/groceries.png" alt="user icon" height="90">
                <p>Groceries</p>
            </td>
            <td class="light"><img src="http://www.teamsaner.com/RMO/fast.png" alt="user icon" height="90">
                <p>Fast Food</p>
            </td>
            <td class="dark"><img src="http://www.teamsaner.com/RMO/dining.png" alt="user icon" height="90">
                <p>Dining Out</p>
            </td>
            <td class="light"><img src="http://www.teamsaner.com/RMO/work.png" alt="user icon" height="90">
                <p>Work Snacks</p>
            </td>
            <td class="dark"><img src="http://www.teamsaner.com/RMO/other.png" alt="user icon" height="90">
                <p>Other</p>
            </td>
        </tr>
        <tr class="border">
            <td colspan="6"></td>
        </tr>
        <tr>
            <td class="light j-user">James</td>
            <td class="dark j-groc"></td>
            <td class="light j-fast"></td>
            <td class="dark j-din"></td>
            <td class="light j-work"></td>
            <td class="dark j-other"></td>
        </tr>
        <tr>
            <td class="light m-user">Mary</td>
            <td class="dark m-groc"></td>
            <td class="light m-fast"></td>
            <td class="dark m-din"></td>
            <td class="light m-work"></td>
            <td class="dark m-other"></td>
        </tr>
        <tr>
            <td class="light k-user">Kathy</td>
            <td class="dark k-groc"></td>
            <td class="light k-fast"></td>
            <td class="dark k-din"></td>
            <td class="light k-work"></td>
            <td class="dark k-other"></td>
        </tr>
        <tr>
            <td class="light s-user">Steve</td>
            <td class="dark s-groc"></td>
            <td class="light s-fast"></td>
            <td class="dark s-din"></td>
            <td class="light s-work"></td>
            <td class="dark s-other"></td>
        </tr>
        <tr>
            <td class="light r-user">Robert</td>
            <td class="dark r-groc"></td>
            <td class="light r-fast"></td>
            <td class="dark r-din"></td>
            <td class="light r-work"></td>
            <td class="dark r-other"></td>
        </tr>
        </table>
    </div><!-- chart -->

    <div class="receipt">
    	<img src="http://www.teamsaner.com/RMO/receipt.jpg">
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
