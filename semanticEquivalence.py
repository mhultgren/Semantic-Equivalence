import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
print("module loaded")


def embed(input):
    return model(input)


continue_input = True

while continue_input:
    messages = []
    print("\nEnter first sentence:", end=" ")
    sentence1 = input()
    print("Enter second sentence:", end=" ")
    sentence2 = input()

    messages.append(sentence1)
    messages.append(sentence2)

    embeddings_matrix = embed(messages)

    similarity_matrix = np.inner(embeddings_matrix, embeddings_matrix)
    # print(similarity_matrix[0][1])

    if float(similarity_matrix[0][1]) > .8:
        print("The sentences you have entered are considered duplicate.")
    else:
        print("The sentences you have entered are considered NOT duplicate.")

    response = ""
    print("Continue?")

    while response != 'y' and response != 'n':
        print(" (Enter 'y' or 'n')", end=" ")
        response = input()

        if response == 'n':
            continue_input = False
