"""
Configuration of vocabulary game server.
Generated Thu Oct 27 18:10:26 PDT 2016
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="01a94f1339fc6706201f34968edb021f"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

