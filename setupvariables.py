# Parameters, variables and constants
#
# May be tuned to increase quality of predicted text or changing the visuals of training.
#
#
#
#####################################

# Parameters for training generative model.
# Quality of predicted text may be increased or decreased immensely if tuning them.
parameters_setup = {
    # If the number of words in a sentence is less than MIN_WORDS, the sentence will not be used.
    # Prevents short non-sense sentences.
    'LEARNING_RATE': 0.07,

    # How many words to look at before altering weights. Low batches may prevent over fit
    'BATCHES': 1,

    # How many words/letter then model will look at while training.
    # Higher = better at remembering, Lower = very precise but cannot remember.
    'BP_LOOK_BACK': 4,

    # Number of nodes. More nodes = model will remember contexts, but causes slower training.
    'NODES': 700
}


# Pre Processing variables are responsible for quality of input.
# Second most important parameters to tune to increase quality.
preprocess_setup = {

    # If the number of words in a sentence is less than MIN_WORDS, the sentence will not be used.
    # Prevents short non-sense sentences.
    'MIN_WORDS': 5,

    # If a word appears less than WORD_THRESHOLD in processing, the sentence will not be used
    # Prevents less occurring words and highers quality of processing
    # If you have a small processing set, this must be lowered
    # Try to get at maximum 3k unique words. Having more slows down word2vec EXTREMELY
    'WORD_THRESHOLD': 40,

    # If 'words' generate words, if 'letters' use letters instead.
    # Increase MIN_WORDS if using 'letters'.
    'TRAINING_TYPE': 'words'
}


# Word2vec trains dense vector representation of words instead of sparse vectors.
word2vec_params_setup = {

    # Number of words/letters to predict each time
    'EMBEDDING_SIZE': 300,

    # How many batches per change of weights. Recommended: 1
    'BATCHES': 1,

    # Number of epochs to train. One epoch = going through all text once
    'EPOCHS': 10,

    # Only for testing. Instantly finishes word2vec training.
    'SHORT_MODE': True,

    # Learning step size
    'LEARNING_RATE': 0.2,

    # Number of iterations before LR decreases and word2vec verbose
    'ITERATIONS_BEFORE_LR_DECREASE': 50,

    # For every ITERATIONS_BEFORE_LR_DECREASE multiply LEARNING_RATE with this constant
    # The LR_DECREASE should at the end of training make LEARNING_RATE be around 1/1000 its initial value
    # To calculate a optimal decrease:
    # dataset_size(total iters) / ITERATIONS_BEFORE_LR_DECREASE = number_of_decreases
    # LR_DECREASE ^ number_of_decreases = 0.001
    'LR_DECREASE': 0.96
}

# Parameters for testing of word embedding representations.
# (Does not affect quality of generator. Only visual.)
test_emb_setup = {
    # If true, when starting to train, a number of NUM_TEST_EMBEDDINGS embeddings will be tested.
    'USE_TEST_EMBEDDINGS': True,

    # Number of randomly chosen tested embeddings.
    'NUM_TEST_EMBEDDINGS': 3,

    # List of words to check similarities every time.
    # Recommended to have at least one pair of very similar words like (he, she) which are interchangeable
    # and one pair of not similar words such as (almost, tv), can rarely be used in each others positions.
    'TESTING_WORDS': [('he', 'she'), ('almost', 'tv')],

    # If True, verbose cosine distance between words when training
    'VERBOSE_COSINE': True
}

# Setup for predicting. Affects log output.
# (Does not affect quality of generator. Only visual.)
predict_setup = {
    # Number of words/letters to predict each time
    'SAMPLES': 15,

    # Seconds between every output.
    'SECONDS_BETWEEN_PREDICT': 15
}