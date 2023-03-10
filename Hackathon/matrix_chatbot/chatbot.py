from chatterbot import ChatBot

chatbot = ChatBot(
    'MAtrix',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/q_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_q.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

trainer.export_for_training('./my_export1.json')

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english.greetings',
    'chatterbot.corpus.english.conversations'
)

# # Now we can export the data to a file
# trainer_corpus.export_for_training('./my_export.json')
