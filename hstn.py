class hstn():
    
    # creating the constructor
    def __init__(self):
        # initiating the interaction counter
        self._interaction_counter = 0
        # initiating user engagement
        self.user_input = []
        self.currentSuperStateTransition = False
        self.userEngagement = 0
        self.userOpinion_positive = []
        self.nextSuperState = 2 # 0: supporting user; 1: listening to user; 2: main task
        self.number_of_interactions_fixed = 6
        # defining list to store sentences in the list
        self._about_lecture = []
        self._task_organization = []
        self._student_interaction = []
        self._clarity = []
        # defining an end key to exit from the interaction by typing the 'quit' keyword;  once 'quit' is typed the logic turned from True to False
        self.end_key = True
        
        
    @property
    def interaction_counter(self):
        return self._interaction_counter

    @interaction_counter.setter
    def interaction_counter(self, value):
        self._interaction_counter = value
        
    @property
    def about_lecture(self):
        return self._about_lecture

    @about_lecture.setter
    def about_lecture(self, sentences):
        self._about_lecture = sentences
        self.reset_interaction_counter() 
        # Resetting interaction counter when setting about_lecture
    
        
    @property
    def task_organization(self):
        return self._task_organization
    
    @task_organization.setter
    def task_organization(self, sentences):
        self._task_organization = sentences
        self.reset_interaction_counter() 
    
        
    @property
    def student_interaction(self):
        return self._student_interaction
    
    @student_interaction.setter
    def student_interaction(self, sentences):
        self._student_interaction = sentences
        self.reset_interaction_counter() 
    
        
    @property
    def clarity(self):
        return self._clarity
    
    @clarity.setter
    def clarity(self, sentences):
        self._clarity = sentences
        self.reset_interaction_counter() 
    
    def reset_interaction_counter(self):
        self._interaction_counter = 0
        self.currentSuperStateTransition = False
              
    # rules
    # first system looks for 6 interactions
    # after the a superstate breaks, switches to other superstate then, it willl looks for next three interactions before making IM decision 
    
    def define_model(self):

        GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY_1")

        # Configure the client library by providing your API key.
        genai.configure(api_key=GOOGLE_API_KEY)

        model = 'gemini-1.0-pro' # @param {isTemplate: true}
        contents_b64 = 'W3sicm9sZSI6InVzZXIiLCJwYXJ0cyI6ImdldCBtZSBhIG1vdGl2YXRpb25hbCBxdW90ZSJ9LHsicm9sZSI6Im1vZGVsIiwicGFydHMiOiJcIlRoZSBvbmx5IHBlcnNvbiB5b3UgYXJlIGRlc3RpbmVkIHRvIGJlY29tZSBpcyB0aGUgcGVyc29uIHlvdSBkZWNpZGUgdG8gYmUuXCIgLSBSYWxwaCBXYWxkbyBFbWVyc29uIn1d' # @param {isTemplate: true}
        generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC41LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119' # @param {isTemplate: true}
        safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}
        user_input_b64 = '' # @param {isTemplate: true}

        contents = json.loads(base64.b64decode(contents_b64))
        generation_config = json.loads(base64.b64decode(generation_config_b64))
        safety_settings = json.loads(base64.b64decode(safety_settings_b64))
        user_input = base64.b64decode(user_input_b64).decode()
        stream = False
        
        generation_config['temperature'] = 1.0

        return (model, contents)
    
    def generate(self, user_input, model, contents, stream=False):

        # Call the model and print the response.
        gemini = genai.GenerativeModel(model_name=model)

        chat = gemini.start_chat(history=contents)

        response = chat.send_message(
            user_input,
            stream=stream)

        return (response.text)
        
    def summarize(self, sample_text, max_length=30, min_length=25):

        summaries = {}

        # Initialize the pipeline for text generation
        pipe = pipeline("summarization", model="t5-large")

        pipe_out = pipe(sample_text, max_length=max_length, min_length=min_length)

        # generating summaries
        summaries["t5"] = "".join(sent_tokenize(pipe_out[0]["summary_text"]))

        return(summaries["t5"])


    # Main state - Greeting
    def greeting(self):
        greeting_responses = ["Hi!! Buddy, let's talk about your recent lecture experience",
                                "Good morning, let's talk about your recent lecture experience",
                                "Hey, what's up?, let's talk about your recent lecture experience",
                                "Greetings!, let's talk about your recent lecture experience",                      
                                "Hey, nice to meet you!, let's talk about your recent lecture experience",
                                "Hey, it's great to see you!!, let's talk about your recent lecture experience"]

        print (greeting_responses[rn.randint(0,len(greeting_responses)-1)])
        
    # keeping the record of the starting time of the interaction
    def get_task_starting_time(self):
        # make a note on starting time
        now = datetime.now()
        return (now)
    
    # keeping the record of the ending time of the interaction
    def get_task_ending_time(self):
        # make a note on ending time
        end = datetime.now()
        return (end)
    
    # get the time required for the task completion
    def get_task_completion_time(self, start, end):
        # getting the difference of time in seconds
        delta_time = (end - start).seconds
        # printing the time taken by the uer to accomplish the task
        print (f"The time taken by the user to accomplish the task is: {delta_time} seconds")
        # writing the time taken by the user to the text file for log keeping
        with open("user#04_time_taken.txt", "w") as file:
            file.write("The time taken by the user to accomplish the task is: " + str(delta_time) + " " + "seconds")
        
    # listeing to user
    def listening_to_user(self):
        # initiating the model
        model, contents = self.define_model()
        # define the prompt (the context) to generate the text
        recent_interactions = self.user_input[-6:]
        recent_interactions_as_string = " ".join(recent_interactions)
        # prompt design for getting the summary only in sentence form
        summarize_prompt = "summarize the following sentence in sentence form:" + " " + recent_interactions_as_string
        # feeding the prompt into the gemini LLM
        recent_summary =  self.generate(summarize_prompt, model, contents, stream=False) #self.summarize(recent_interactions_as_string)
        # theme responses 
        pre_defined_responses_list = ["I understood your thoughts correctly right, what do you feel?",
                                 "Please share more about your opinion, that will be useful for future students?",
                                     "Please share something about if you had any inconvenience during the lecture"]
        pre_defined_responses = []
        for i in range(len(pre_defined_responses_list)):
            pre_defined_responses.append(pre_defined_responses_list[rn.randint(1,3)-1])
        
        # creating a followup list
        follow_up = []
        # looping through the responses and paraphrasing the responses
        for sent in pre_defined_responses:
            follow_up_prompt = "refine the following text and rewrite in only one sentence:" + " " + sent
            follow_up.append(self.generate(follow_up_prompt, model, contents, stream=False)) 
        return recent_summary, follow_up
    

    # supporting to user
    def Supporting_user(self, sentence):
        # definig supporting user list
        supporting_user = []
        model, contents = self.define_model()
        for i in range(3):
            supporting_user.append(self.generate(sentence, model, contents, stream=False))
        return supporting_user
    
    # Main state - Concluding
    def reflecting_and_concluding(self):
        # getting all of the uresponses of the user in a list
        user_responses = self.get_user_response()
        usr_res_str = " ".join(user_responses)
        model, contents = self.define_model()
        # prompt design for getting the summary only in sentence form
        reflc_prompt = "summarize the following sentence in sentence form as a final refelction of the whole interaction:" + " " + usr_res_str
        # feeding the prompt into the gemini LLM
        reflc_res =  self.generate(reflc_prompt, model, contents, stream=False) #self.summarize(recent_interactions_as_string)
        
        # middle sentence
        mid_sent = "All of the responses you gave were recorded carefully and your details have been completely anonymized. This is what I have got with the interaction we had,"
        # ending sentence
        end_sent = "Thank you again for sharing your thoughts with me. See you next time."
        
        concluding_responses = ["Thank you for your insights and valuable input. Your perspective is greatly appreciated", "I appreciate your time and thoughtful responses. Thank you for sharing your thoughts with me",
                                "Thank you for taking the time to discuss these matters with me. Your input has been instrumental", "I'm grateful for the opportunity to hear your thoughts on this. Thank you for your time and thoughtful contributions",
                                "Your time and expertise are highly valued. Thank you for engaging in this discussion with me", "Thank you for spending your valuable time sharing your experiences and opinions. It has been a meaningful conversation",
                                "I want to express my gratitude for your time and the enriching conversation we've had. Thank you for your insights", "Thank you for your thoughtful responses. Your time and input have been invaluable to this discussion",
                                "I appreciate the depth of our conversation. Thank you for dedicating your time and sharing your perspective with me", "Thank you for your time and openness in discussing these matters. It has been a pleasure engaging in this conversation with you"]
        print (concluding_responses[rn.randint(0,len(concluding_responses)-1)] + "." + " " + mid_sent + " " + reflc_res + end_sent)
        

   # calulating the fuzzy output value considering emotional cue and user engagement as input
    def calc_fuzzy(self, val1, val2):
        # A simple fuzzy inference system for the tipping problem
        # A simple fuzzy inference system for the tipping problem
        # Create a fuzzy system object
        FS = simpful.FuzzySystem()

        # Define fuzzy sets and linguistic variables
        S_1 = simpful.FuzzySet(points=[[0., 1.], [0.19, 1.], [0.49, 0.0]], term='Negative')
        S_2 = simpful.FuzzySet(points=[[0.344 , 0.], [0.503 , 1.], [0.6549, 0.]], term="Neutral")
        S_3 = simpful.FuzzySet(points=[[0.5011, 0.], [0.798 , 1.], [1., 1.]], term="Positive")
        FS.add_linguistic_variable("Emotion", simpful.LinguisticVariable([S_1, S_2, S_3], concept="Recent Emotion", universe_of_discourse=[0,1]))

        F_1 = simpful.FuzzySet(points=[[0., 1.], [0.097, 1.0], [0.2974, 0]], term="Very_low")
        F_2 = simpful.FuzzySet(points=[[0.1035, 0.0], [0.34, 1.0], [0.49, 0.0]], term="Low")
        F_3 = simpful.FuzzySet(points=[[0.4, 0.0], [0.5, 1], [0.6008, 0.0]], term="Medium")
        F_4 = simpful.FuzzySet(points=[[0.545, 0.0], [0.758, 1.0], [0.9247, 0.0]], term="High")
        F_5 = simpful.FuzzySet(points=[[0.702, 0.0], [0.9009, 1], [1.0, 1.0]], term="Very_High")
        FS.add_linguistic_variable("Engagement", simpful.LinguisticVariable([F_1, F_2, F_3, F_4, F_5], concept="User Engagement", universe_of_discourse=[0,1]))

        # Define output crisp values
        FS.set_crisp_output_value("Supporting", 0.1)
        FS.set_crisp_output_value("Listening", 0.5)
        FS.set_crisp_output_value("Main", 1.0)

        # Define function for generous tip (food score + service score + 5%)
        #FS.set_output_function("generous", "Food+Service+5")

        # Define fuzzy rules
        R1 = "IF (Emotion IS Negative) AND (Engagement IS Very_low) THEN (Tip IS Supporting)"
        R2 = "IF (Emotion IS Negative) AND (Engagement IS Low) THEN (Tip IS Supporting)"
        R3 = "IF (Emotion IS Negative) AND (Engagement IS Medium) THEN (Tip IS Supporting)"
        R4 = "IF (Emotion IS Negative) AND (Engagement IS High) THEN (Tip IS Listening)"
        R5 = "IF (Emotion IS Negative) AND (Engagement IS Very_High) THEN (Tip IS Listening)"
        R6 = "IF (Emotion IS Neutral) AND (Engagement IS Very_low) THEN (Tip IS Supporting)"
        R7 = "IF (Emotion IS Neutral) AND (Engagement IS Low) THEN (Tip IS Supporting)"
        R8 = "IF (Emotion IS Neutral) AND (Engagement IS Medium) THEN (Tip IS Listening)"
        R9 = "IF (Emotion IS Neutral) AND (Engagement IS High) THEN (Tip IS Main)"
        R10 = "IF (Emotion IS Neutral) AND (Engagement IS Very_High) THEN (Tip IS Main)"
        R11 = "IF (Emotion IS Positive) AND (Engagement IS Very_low) THEN (Tip IS Supporting)"
        R12 = "IF (Emotion IS Positive) AND (Engagement IS Low) THEN (Tip IS Supporting)"
        R13 = "IF (Emotion IS Positive) AND (Engagement IS Medium) THEN (Tip IS Listening)"
        R14 = "IF (Emotion IS Positive) AND (Engagement IS High) THEN (Tip IS Main)"
        R15 = "IF (Emotion IS Positive) AND (Engagement IS Very_High) THEN (Tip IS Main)"
        FS.add_rules([R1, R2, R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15])


        # Set antecedents values
        FS.set_variable("Emotion", val1)
        FS.set_variable("Engagement", val2)

        # Perform Sugeno inference and print output
        return(FS.Sugeno_inference(["Tip"]))
    
    # defining function for getting sentiment of user 
    def get_sentiment(self, sequence_to_classify, candidate_labels = ['positive', 'negative']):
        classifier = pipeline("zero-shot-classification",
                          model="facebook/bart-large-mnli")
        sentiment = classifier(sequence_to_classify, candidate_labels)
        labels = sentiment['labels']
        sentiment_scores = sentiment['scores']
        corresponding_index = np.argmax(sentiment_scores)
        return (labels[corresponding_index])
    
    # defining a function for calculating user engagement ==> based on 1st Quartile
    def calc_user_eng_quart(self, array):
        # assuming array consists of all the user responses
        last_six_int = array[-6:]
        # getting num.of words in last 6 interactions
        num_words = []
        # a way if getting total number of words in recent 6 interactions
        for i in last_six_int:
            words = i.split()
            num_words.append(len(words))
        # getting number of long responses
        # here we are assuming that the long responses are the the responses that has the sentence length greater than 1st quartile
        long_response = 0
        # getting the 1st quartile of recent 6 interactions
        q3, q2, q1 = np.percentile(num_words, [75,50,25])
        # q1: 1st quartile lenth of responses
        for i in last_six_int:
            if (len(i.split()) >= q1):
                long_response = long_response + 1
        return (long_response / 6)
    
    # defining a function for calculating user engagement ==> based on mean
    def calc_user_eng(self, array):
        # assuming array consists of all the user responses
        last_six_int = array[-6:]
        # total words in last 6 interactions
        total_words = 0
        # a way if getting total number of words in recent 6 interactions
        for i in last_six_int:
            words = i.split()
            total_words = total_words + len(words)
        # getting number of long responses
        long_response = 0
        for i in last_six_int:
            if len(i.split()) >= (total_words / 6):
                long_response = long_response + 1
        return (long_response / 6)
    
    # defining a function for calculating user opinon
    def calc_user_opn(self, array):
        # assuming array consist of all of the user opnions for their responses
        last_six_int = array[-6:]
        # the above have a mix of 'positive' and 'negative'
        pos_opn = 0
        for i in last_six_int:
            if i == "positive":
                pos_opn = pos_opn + 1
        return (pos_opn / 6)

    # a method to loop through all sentences in a list ==> System A
    def loop_all_system_A(self, sentence, superstate_number):
        #print (type(sentence))
        # checking the end_key at the initial stage of each superstate if it is True it allows to gr through all local states
        if (len(sentence) > 0 and self.end_key):
            for i in sentence:
                # checking the end_key at each iteration within a specified superstate, if ture pass to next local state otherwise break the loop
                if self.end_key:
                    print (i)
                    user_input_instant = self.get_user_input()
                    opinion = self.get_sentiment(user_input_instant)
                    print (opinion)
                    self.userOpinion_positive.append(opinion)

                    self.interaction_counter = self.interaction_counter + 1
                    # printing the value of interaction_counter
                    print (f"Value of interaction counter: {self.interaction_counter}")
                    if ((self.interaction_counter) >= self.number_of_interactions_fixed):

                        # once the number of interaction exceeded 6 then system looks for next 3 interactions before changing interaction mode
                        #self.number_of_interactions_fixed = 6

                        # getting interaction modes
                        self.state_switch(self.userOpinion_positive, self.user_input, self.currentSuperStateTransition)

                        # decison making based on interaction modes
                        if (self.nextSuperState == 2):
                            pass

                        elif (self.nextSuperState == 1):
                            model, contents = self.define_model()
                            self.interaction_counter = 0
                            recent_summary, follow_up = self.listening_to_user()
                            listening_list = ["I understand that" + " " + recent_summary + " " + "and" + " " + "I agree with your opinion and what you feel about is totally fine."]
                            #pre_defined_responses = ["Please share more about your opinion, that will be useful for future students",
                            #"Feel free to talk about any inconvenience you have"]
                            listening_list.extend(follow_up)
                            self.loop_all_system_A(listening_list, superstate_number)

                        elif (self.nextSuperState == 0):
                            self.interaction_counter = 0
                            # tracking the main task superstate
                            #1 = about lecture
                            #2 = task organization
                            #3 = student interaction
                            #4 = clarity

                            if superstate_number == 1:
                                prompt_supporting_user = "Students are having problems in understanding the concepts in the lecture. Assume yourself as a friend talking directly to the students and give some advice in a very short sentence, not in bullet point form, only in one sentence."
                            elif superstate_number == 2:
                                prompt_supporting_user = "Students are having problems in the organization of the lecture such as spped of lecture, organizaion of topics and flow etc. Assume yourself as a friend talking directly to the students and give some advice in a very short sentence, not in bullet point form, only in one sentence."
                            elif superstate_number == 3:
                                prompt_supporting_user = "Students are having problems in professor's approach of making an interesting student interaction like asking open questions to the class and encourage students to share their thoughts on the subject related matter. Assume yourself as a friend talking directly to the students and give some advice in a very short sentence, not in bullet point form, only in one sentence."
                            else:
                                prompt_supporting_user = "Students are having problems in the clarity of the lecture such as audibility, visuals of presentation slides etc. Assume yourself as a friend talking directly to the students and give some advice in a very short sentence, not in bullet point form, only in one sentence."


                            # define the prompt (the context) to generate the text
                            supporting_user_list = self.Supporting_user(prompt_supporting_user)
                            self.loop_all_system_A(supporting_user_list, superstate_number)

                        elif (self.nextSuperState == 3):
                            break

                        else:
                            pass
                else:
                    # break from the loop once the end_key identified as False due to quit keyword typed by the user
                    break
        else:
            # ignoring the empty list 
            pass

    # defining state switching condition
    def state_switch(self, userOpinion, userEngagement, currentSuperstateTransition):
        userOpinion = self.calc_user_opn(userOpinion)
        print (userOpinion)
        userEngagement = self.calc_user_eng(userEngagement)
        print (userEngagement)
        interactionMode = self.calc_fuzzy(userOpinion, userEngagement)
        interactionMode = interactionMode['Tip']
        print (interactionMode)
        if currentSuperstateTransition == False:

            if interactionMode <= 0.20:
                self.nextSuperState = 0
                self.currentSuperStateTransition = True
            elif interactionMode <= 0.74:
                self.nextSuperState = 1
                self.currentSuperStateTransition = True
            else:
                self.nextSuperState = 2
        else:
            if interactionMode <= 0.74:
                self.nextSuperState = 3 # 3: denotes to break from the current super state and switch to the next direct superstate
                self.currentSuperStateTransition = False
                self.interaction_counter = 3
                
            else:
                self.nextSuperState = 2 # 2: go ahead with the main task
                       

    # map the superstate to its numerical value
    def map_superstate_2_number(self, text):
        text = text.lower()
        superstate_to_number = {"about": 1, "task": 2, "student": 3, "clarity": 4}
        return (superstate_to_number[text])
    
    # run the overall system ==> For System A
    def run_system_A(self):
        start_time = self.get_task_starting_time()
        self.greeting()
        self.get_user_input()
        self.reset_interaction_counter()
        self.loop_all_system_A(self.about_lecture, self.map_superstate_2_number("About"))
        self.reset_interaction_counter()
        self.loop_all_system_A(self.task_organization, self.map_superstate_2_number("Task"))
        self.reset_interaction_counter()
        self.loop_all_system_A(self.student_interaction, self.map_superstate_2_number("Student"))
        self.reset_interaction_counter()
        self.loop_all_system_A(self.clarity, self.map_superstate_2_number("Clarity"))
        self.reflecting_and_concluding()
        end_time = self.get_task_ending_time()
        # calling the function to get the time difference and save it to a text file
        self.get_task_completion_time(start_time, end_time)
        
    # get the user input
    def get_user_input(self):
        user_input_instant = input("Type your response here: ")
        # checking for the keyword quit and change the logic of end_key accordingly so as to end the interaction since the user is not intended to continue
        if user_input_instant.lower() == "quit":
            self.end_key = False
        else:
            self.user_input.append(user_input_instant)
        return user_input_instant

    # getting the user responses at once
    def get_user_response(self):
        return (self.user_input)
