# 🐍 This is the Python code linked to your Dash

# 🔄 Code here is executed at each restart of the app

# 📍 This is the place where you set the initial state of your app...

from API import make_test_request, make_search_request;

name = "OLUKAYODE EXCEL";
counter = 0;

search_term = "";
api_result = "";

# ...and define functions that return data to be displayed...
def display_greeting():
    text = " # DEVELOPMENT OF AN ONTOLOGY BASED INFORMATION RETRIEVAL SYSTEM FOR HOLY BIBLE REFERENCES</center> \n ## <center> BY: OLUKAYODE EXCEL <center/>\n";
    return text;

def display_search_term():
    return  f"##  Search Term: {search_term}";

def display_text_input_label():
    return "## Enter search term:"

def onClick_search_button():
    global api_result;
    print("<-> ========= Search button clicked ========= <->");
    make_test_request();

    data = make_search_request(search_term);

    if (data['status'] == 200):
        text="";

        text = f"> # Searched Term: {data['search_term'].capitalize()}\n";

        if (len(data['synonyms']) > 0): text += f"> # Synonyms: {[synonym.capitalize() for synonym in data['synonyms']]}\n";

        references = data['biblical_references'];

        if ( len(references) > 0):

            text += f"> # Biblical References: {references[0]['bookref']}\n";

            del references[0];

            for reference in references:
                text += f"> #          \t\t\t           : {reference['bookref']}\n";

    else:
        text = "# <center>Oops</center> \n ## <center>Information Not Found!</center>";

    api_result = text;


def result_display():
    return api_result;

# ...or that handle user input
def increment():
    global counter
    counter += 1


# 🔗 Everything defined here is available to use on the Layout Editor
