<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="css/version1.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <title>WikiFlash</title>
  </head>
  <body>
    <div id='container_id' class="container">
      <div class="logo_box">
        <img id='flash_logo' class='logo' src="images/manta-ray-black-silhouette.jpg" alt="logo">
      </div>
      <div class="word_input">
        <form action="/action_page.py">
          <input type="text" id="fname" name="firstname" placeholder="Your start word..">
          <input type="text" id="lname" name="lastname" placeholder="Your end word..">
          <input id='submit_it' type="button" value="Submit">
        </form>
      </div>
    </div>
  </div>

  <div class="display_wrapper">
    <div class="status_box_id" id='status_box_id'>
        <h3 id='demo'></h3>
        <div class="">

        </div>
        <div class="">

        </div>
        <div class="">

        </div>
        <div class="">

        </div>
        <button id="return_button" type="button" name="button" value="Refresh Page" onClick="refresh">Return</button>
    </div>
  </div>
    <script src="jsfolder\first.js"></script>
  </body>
</html>
