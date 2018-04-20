from __future__ import print_function

dx = [0,-1,0,1]
dy = [-1,0,1,0]

arr = [

      [1,1,1,1,1],
      [0,1,0,1,0],
      [0,1,0,1,0],
      [0,1,0,1,0],
      [1,1,1,1,1],

      ]


current_x = 0
current_y = 0
prev_x = 0
prev_y = 0




# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

#------------------------------------------------------------------------------


def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the  Maze Game. " \
                    "Lets start the journey by moving forward."
    reprompt_text = "Please initiate the game."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for playing The Maze Game. " \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def create_attribute(favorite_color):
    return {"Direction": favorite_color}


def bfs(intent, session):

    card_title = intent['name']
    session_attributes={}
    should_end_session = False
    global current_x
    global current_y
    global dx
    global dy

    row = len(arr)
    col = len(arr[0])

    ix = current_x
    jy = current_y

    dist = [[0 for x in range(col)] for y in range(row)]
    visit = [[False for x in range(col)] for y in range(row)]

    visit[ix][jy]=True
    dist[ix][jy]=0
    queue = [(ix,jy)]
    while queue:

        (x,y) = queue.pop(0)

        for i,j in zip(dx,dy):
            if(x+i>=0 and x+i<=row-1 and y+j>=0 and y+j<=col-1 and arr[x+i][y+j]==1 and visit[x+i][y+j]==False):
                dist[x+i][y+j]=dist[x][y]+1
                visit[x+i][y+j]=True
                queue.append((x+i,y+j))


    speech_output = "You are "+ str(dist[row-1][col-1]) + " units away from finishing your journey ."

    reprompt_text = "Hint was already given, continue the journey ."


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def AskNow(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    global current_x
    global current_y
    global prev_x
    global prev_y
    rr , ll ,ff , bb = False,False,False,False
    row = len(arr)
    col = len(arr[0])

    if(current_x == prev_x and prev_y <= current_y):

        if(current_x>=0 and current_x<row-1 and current_y>=0 and current_y<=col-1 and arr[current_x+1][current_y]==1):
            rr = True
        if(current_x>=0 and current_x<=row-1 and current_y>=0 and current_y<col-1 and arr[current_x][current_y+1]==1):
            ff = True
        if(current_x>0 and current_x<=row-1 and current_y>=0 and current_y<=col-1 and arr[current_x-1][current_y]==1):
            ll = True
        if(current_x>=0 and current_x<=row-1 and current_y>0 and current_y<=col-1 and arr[current_x][current_y-1]==1):
            bb = True

    elif(current_x == prev_x and prev_y > current_y):

        if(current_x>0 and current_x<=row-1 and current_y>=0 and current_y<=col-1 and arr[current_x-1][current_y]==1):
            rr = True
        if(current_x>=0 and current_x<=row-1 and current_y>0 and current_y<=col-1 and arr[current_x][current_y-1]==1):
            ff = True
        if(current_x>=0 and current_x<row-1 and current_y>=0 and current_y<=col-1 and arr[current_x+1][current_y]==1):
            ll = True
        if(current_x>=0 and current_x<=row-1 and current_y>=0 and current_y<col-1 and arr[current_x][current_y+1]==1):
            bb = True

    elif(prev_y == current_y and prev_x <= current_x):

        if(current_x>=0 and current_x<=row-1 and current_y>0 and current_y<=col-1 and arr[current_x][current_y-1]==1):
            rr = True
        if(current_x>=0 and current_x<row-1 and current_y>=0 and current_y<=col-1 and arr[current_x+1][current_y]==1):
            ff = True
        if(current_x>=0 and current_x<=row-1 and current_y>=0 and current_y<col-1 and arr[current_x][current_y+1]==1):
            ll = True
        if(current_x>0 and current_x<=row-1 and current_y>=0 and current_y<=col-1 and arr[current_x-1][current_y]==1):
            bb = True

    elif(prev_y == current_y and prev_x > current_x):

        if(current_x>=0 and current_x<=row-1 and current_y>=0 and current_y<col-1 and arr[current_x][current_y+1]==1):
            rr = True
        if(current_x>0 and current_x<=row-1 and current_y>=0 and current_y<=col-1 and arr[current_x-1][current_y]==1):
            ff = True
        if(current_x>=0 and current_x<=row-1 and current_y>0 and current_y<=col-1 and arr[current_x][current_y-1]==1):
            ll = True
        if(current_x>=0 and current_x<row-1 and current_y>=0 and current_y<=col-1 and arr[current_x+1][current_y]==1):
            bb = True


    s = "You can move to Directions "

    if(rr == True):
        s = s + "Right ,"
    if(ll == True):
        s = s + "Left ,"
    if(ff == True):
        s = s + "Forward ,"
    if(bb == True):
        s = s + "Backward ,"

    s = s[:-1]

    speech_output = s
    reprompt_text = "Help was already given, continue the journey ."


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def set_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """
    global current_x
    global current_y
    global prev_x
    global prev_y


    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    speech_output = ""

    row = len(arr)
    col = len(arr[0])


   # print(str(current_x)+' '+str(current_y)+' '+str(prev_x)+' '+str(prev_y))


    if 'Right' in intent['slots']:
      #  favorite_color = intent['slots']['Right']['value']
        favorite_color='Right'
        session_attributes = create_attribute(favorite_color)


        if(current_x == prev_x and prev_y <= current_y):
            if(current_y>=0 and current_y<=col-1 and current_x<row-1 and current_x>=0 and arr[current_x+1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x+1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_x == prev_x and prev_y > current_y):
            if(current_y>=0 and current_y<col-1 and current_x<=row-1 and current_x>0 and arr[current_x-1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x-1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x <= current_x):
            if(current_y>0 and current_y<=col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y-1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y-1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x > current_x):
            if(current_y>=0 and current_y<col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y+1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y+1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        else:
            speech_output = "Cannot Proceed Further As we have reached a dead end ."\


        if(current_x == row-1 and current_y == col-1):
            session_attributes={}
            should_end_session=True
            reprompt_text=None
            speech_output="Congratuations . Your journey has ended ."+\
                          "You played well."
            return build_response(session_attributes, build_speechlet_response(
               intent['name'], speech_output, reprompt_text, should_end_session))



        reprompt_text = "Lets continue our journey!! "+\
                        "Where you want to head next?"

    elif 'Left' in intent['slots']:
        #favorite_color = intent['slots']['Left']['value']
        favorite_color='Left'
        session_attributes = create_attribute(favorite_color)


        if(current_x == prev_x and prev_y <= current_y):
            if(current_y>=0 and current_y<=col-1 and current_x<=row-1 and current_x>0 and arr[current_x-1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x-1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_x == prev_x and prev_y > current_y):
            if(current_y>=0 and current_y<=col-1 and current_x<row-1 and current_x>=0 and arr[current_x+1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x+1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x <= current_x):
            if(current_y>=0 and current_y<col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y+1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y+1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x > current_x):
            if(current_y>0 and current_y<=col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y-1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y-1
                speech_output = "So we have taken a  " + \
                                 favorite_color + \
                                " turn  " \
                                "Lets continue!!"
            else:
                speech_output = "Cannot proceed in this direction ."

        else:
            speech_output = "Cannot Proceed Further As we have reached a dead end ."\


        if(current_x==row-1 and current_y==col-1):
            session_attributes={}
            should_end_session=True
            reprompt_text=None
            speech_output="Congratuations . Your journey has ended ."+\
                          "You played well."
            return build_response(session_attributes, build_speechlet_response(
               intent['name'], speech_output, reprompt_text, should_end_session))


        reprompt_text = "Lets continue our journey!! "+\
                            "Where you want to head next?"

    elif 'Forward' in intent['slots']:
        #favorite_color = intent['slots']['Forward']['value']
        favorite_color='Forward'
        session_attributes = create_attribute(favorite_color)



        if(current_x == prev_x and prev_y <= current_y):
            if(current_y>=0 and current_y<col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y+1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y+1
                speech_output = "So we are going  " + \
                                 favorite_color + \
                                " . Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_x == prev_x and prev_y > current_y):
            if(current_y>0 and current_y<=col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y-1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y-1
                speech_output = "So we are going   " + \
                                 favorite_color + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x <= current_x):
            if(current_y>=0 and current_y<=col-1 and current_x<row-1 and current_x>=0 and arr[current_x+1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x+1
                speech_output = "So we are going    " + \
                                 favorite_color + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x > current_x):
            if(current_y>=0 and current_y<=col-1 and current_x<=row-1 and current_x>0 and arr[current_x-1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x-1
                speech_output = "So we are going    " + \
                                 favorite_color + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."
        else:
            speech_output = "Cannot Proceed Further As we have reached a dead end ."\



        if(current_x == row-1 and current_y == col-1):
            session_attributes={}
            should_end_session=True
            reprompt_text=None
            speech_output="Congratuations . Your journey has ended ."+\
                          "You played well."
            return build_response(session_attributes, build_speechlet_response(
               intent['name'], speech_output, reprompt_text, should_end_session))


        reprompt_text = "Lets continue our journey!! "+\
                        "Where you want to head next?"

    elif 'Backward' in intent['slots']:
        #favorite_color = intent['slots']['Backward']['value']
        favorite_color='Backward'
        session_attributes = create_attribute(favorite_color)



        if(current_x == prev_x and prev_y <= current_y):
            if(current_y>0 and current_y<=col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y-1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y-1
                speech_output = "So we have turned around   " + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_x == prev_x and prev_y > current_y):
            if(current_y>=0 and current_y<col-1 and current_x<=row-1 and current_x>=0 and arr[current_x][current_y+1]==1):
                prev_x = current_x
                prev_y = current_y
                current_y=current_y+1
                speech_output = "So we have turned around   " + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x <= current_x):
            if(current_y>=0 and current_y<=col-1 and current_x<=row-1 and current_x>0 and arr[current_x-1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x-1
                speech_output = "So we have turned around   " + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        elif(current_y == prev_y and prev_x > current_x):
            if(current_y>=0 and current_y<=col-1 and current_x<row-1 and current_x>=0 and arr[current_x+1][current_y]==1):
                prev_x = current_x
                prev_y = current_y
                current_x=current_x+1
                speech_output = "So we have turned around   " + \
                                ". Lets continue our journey"
            else:
                speech_output = "Cannot proceed in this direction ."

        else:
            speech_output = "Cannot Proceed Further As we have reached a dead end ."\


        if(current_x==row-1 and current_y==col-1):
            session_attributes={}
            should_end_session=True
            reprompt_text=None
            speech_output="Congratuations . Your journey has ended ."+\
                          "You played well."
            return build_response(session_attributes, build_speechlet_response(
               intent['name'], speech_output, reprompt_text, should_end_session))


        reprompt_text = "Lets continue our journey!! "+\
                        "Where you want to head next?"
    else:
        speech_output = "Lets continue our journey!!"
        reprompt_text = "Please repeat again where are we heading??"


    #print(str(current_x)+' '+str(current_y)+' '+str(prev_x)+' '+str(prev_y))


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


#-----------Events------------------------------------------------------------


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    #temp = intent_request['intent']['name']['slots']['name']
    # Dispatch to your skill's intent handlers
    if intent_name == "MoveRight":
        return set_session(intent, session)
    elif intent_name == "MoveLeft":
        return set_session(intent, session)
    elif intent_name == "MoveForward":
        return set_session(intent, session)
    elif intent_name == "MoveBackward":
        return set_session(intent, session)
    elif intent_name == "Help":
        return AskNow(intent, session)
    elif intent_name == "Hint":
        return bfs(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here
    global current_x
    global current_y
    global prev_x
    global prev_y
    current_x = 0
    current_y = 0
    prev_x = 0
    prev_y = 0



#------------Main Handler------------------------------------------------------

def lambda_handler(event, context):
    # TODO implement
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
