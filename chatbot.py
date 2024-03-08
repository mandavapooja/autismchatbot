# Paste your chatbot code here
import re
import random

# Define conversational pairs related to autism awareness
autism_conversational_pairs = {

    "definition": ["Autism, or autism spectrum disorder (ASD), refers to a range of conditions characterized by challenges with social skills, repetitive behaviors, and communication difficulties.",
                   "Autism is a developmental disorder that affects how a person interacts with others and experiences the world."],
    "causes": ["The exact cause of autism is still not fully understood, but it is believed to involve a combination of genetic and environmental factors.",
                      "There is no single cause of autism, and research suggests that a combination of genetic and environmental influences may contribute to its development."],
    "prevalence": ["According to the Centers for Disease Control and Prevention (CDC), autism affects an estimated 1 in 54 children in the United States.",
                      "Autism prevalence has been increasing in recent years, but this may be due in part to better awareness and diagnosis."],
    "acceptance": ["Autism acceptance emphasizes understanding, respecting, and embracing the differences of individuals with autism.",
                      "Promoting autism acceptance helps create inclusive communities where individuals with autism can thrive and reach their full potential."],
    "advocacy": ["Autism advocacy involves promoting policies and practices that support individuals with autism and their families.",
                    "Advocacy efforts aim to ensure that individuals with autism have access to education, healthcare, employment opportunities, and other resources."],
    "research": ["Ongoing research is essential for advancing our understanding of autism and developing effective interventions and supports for individuals with autism.",
                    "Research in areas such as genetics, brain imaging, and behavioral interventions is helping to improve outcomes for individuals with autism."],
    "symptoms": ["Common symptoms of autism include difficulties in social interaction, communication challenges, repetitive behaviors, and limited interests or activities.",
                    "Autism symptoms can vary widely from person to person, and individuals with autism may exhibit a range of strengths and challenges."],
    "diagnosis": ["Autism diagnosis typically involves a comprehensive evaluation by healthcare professionals, including developmental assessments, interviews, and observation.",
                    "Early diagnosis and intervention are important for improving outcomes for individuals with autism and supporting their overall development."],
    "treatment": ["There is no cure for autism, but early intervention and support services can help individuals with autism lead fulfilling lives.",
                    "Treatment for autism may include behavioral therapy, speech therapy, occupational therapy, and medication to manage symptoms and co-occurring conditions."],
    "education": ["Individuals with autism may benefit from specialized education programs and support services tailored to their unique needs and strengths.",
                    "Inclusive education environments that provide appropriate accommodations and supports can help individuals with autism thrive academically and socially."],
    "communication": ["Communication difficulties are common in individuals with autism and may include challenges with verbal and nonverbal communication.",
                    "Speech therapy and alternative communication methods, such as sign language and picture boards, can help individuals with autism communicate effectively."],
    "social_skills": ["Social skills deficits are a hallmark feature of autism and may include difficulties with understanding social cues, making eye contact, and forming friendships.",
                    "Social skills training programs can teach individuals with autism strategies for interacting with others and navigating social situations."],
    "repetitive_behaviors": ["Repetitive behaviors, such as hand-flapping, rocking, and repetitive speech patterns, are common in individuals with autism and may serve as self-soothing mechanisms.",
                    "Repetitive behaviors in autism can vary in intensity and frequency and may change over time."],
    "sensory_sensitivities": ["Many individuals with autism have sensory sensitivities and may be hypersensitive or hyposensitive to sensory stimuli, such as sounds, lights, textures, and smells.",
                    "Sensory integration therapy and sensory accommodations can help individuals with autism manage sensory sensitivities and regulate their sensory experiences."],
    "co-occurring_conditions": ["Individuals with autism often have co-occurring conditions, such as attention deficit hyperactivity disorder (ADHD), anxiety disorders, and epilepsy.",
                    "Addressing co-occurring conditions is an important part of comprehensive autism care and may involve medication management and behavioral interventions."],
    "early_intervention": ["Early intervention services are crucial for supporting the development and learning of young children with autism.",
                    "Early intervention programs may include speech therapy, occupational therapy, applied behavior analysis (ABA), and developmental therapies."],
    "transition_to_adulthood": ["The transition to adulthood can be challenging for individuals with autism, as they navigate changes in education, employment, housing, and social relationships.",
                    "Transition planning should begin early and involve collaboration between individuals with autism, their families, educators, and service providers."],
    "support_services": ["Various support services are available for individuals with autism and their families, including educational support, vocational training, respite care, and community resources.",
                    "Accessing support services can help individuals with autism lead fulfilling and independent lives."],
    "parenting": ["Parenting a child with autism presents unique joys and challenges, and it's essential for parents to seek support, information, and resources.",
                  "Parenting strategies that emphasize acceptance, understanding, and individualized support can foster positive outcomes for children with autism."],
    "hospitals_in_usa": ["In the USA, there are many hospitals and medical centers that provide specialized care for individuals with autism.",
                         "Some hospitals in the USA offer autism-specific programs and services, including diagnostic evaluations, treatment interventions, and support for families."],
    "encouraging_individuals": ["Encouraging individuals with autism involves recognizing their strengths, providing positive reinforcement, and supporting their interests and passions.",
                                "Offering praise, celebrating achievements, and fostering a supportive environment can boost the confidence and self-esteem of individuals with autism."],
    "providing_help": ["Providing help to individuals with autism may involve offering assistance with daily tasks, providing emotional support, and advocating for their needs.",
                       "Understanding their challenges, respecting their preferences, and offering assistance when needed can make a significant difference in the lives of individuals with autism."]
    # Add more conversational pairs as needed
}

# Add general conversational pairs
general_conversational_pairs = {
    "Hi": ["Hello!", "Hi there!", "Hey! How can I assist you today?"],
    "How are you ": ["fine", "Hi there!,How are you", "Hey! How can I assist you today?"],
    "Bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "about": ["I am a chatbot designed to provide information about autism. Feel free to ask me anything!", "I'm here to help you learn more about autism. Ask me anything!"],
    "random_fact": ["Did you know that autism was first identified in the 1940s by Austrian pediatrician Hans Asperger?", "Here's an interesting fact: Some researchers believe that Leonardo da Vinci may have had autism."],
    # Add more general conversational pairs as needed
}

def chatbot_response(query):
    """
    Generates a response to a user query based on the chosen topic.
    """
    if query.lower() == 'topics':
        topics_list = "\n".join([f"{idx + 1}. {topic.capitalize()}" for idx, topic in enumerate(autism_conversational_pairs.keys())])
        return "Here are the topics you can learn about:" + topics_list

    # Check if the query matches any autism-related topic
    for topic, responses in autism_conversational_pairs.items():
        if re.search(r"\b{}\b".format(topic), query, re.IGNORECASE):
            return random.choice(responses)

    # Check if the query matches any general topic
    for topic, responses in general_conversational_pairs.items():
        if re.search(r"\b{}\b".format(topic), query, re.IGNORECASE):
            return random.choice(responses)

    return "I'm sorry, I'm not sure how to respond to that."
def main():
    print("Welcome to the Autism Awareness Chatbot!\n")  # Add newline character here
    print("Feel free to ask me anything about autism or chat about general topics.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.isdigit():
            idx = int(user_input)
            topics = list(autism_conversational_pairs.keys())
            if 1 <= idx <= len(topics):
                topic = topics[idx - 1]
                response = chatbot_response(topic)
                print("Chatbot:", response)
            else:
                print("Invalid topic number. Please enter a number within the range.")
        elif user_input.lower() == 'topics':
            topics_list = "\n".join([f"{idx + 1}. {topic.capitalize()}" for idx, topic in enumerate(autism_conversational_pairs.keys())])
            print("Here are the topics you can learn about:\n" + topics_list)
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
