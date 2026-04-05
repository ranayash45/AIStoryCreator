from openai import OpenAI, api_key
import openai

storyai = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")
print("Initialize storyAI")
extractorai = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")
print("Initialize extractorAI")
def content_create(style, additional_information):
    response = storyai.chat.completions.create(model="phi3:latest",messages=[{
        "role":"system",
        "content":"""
                A Smart Stroy telling machine which specialize to understand the style of story and requested topic.
                based on topic, AI will try to create complete story around it and perform following steps.

                Steps:
                1. Create Detailed Complete Story
                2. Put Story in <div> tag
                3. Add <style> tag in div to style content according to topic and story style.
                4. Apply style only on story class
                5. Add background color like book and borders with padding to div to make text readable
                6. Choose fonts
                7. refine everything
                8. show the final story in <div> tag

                Rules:
                1. Story must inside div tag along with head line
                2. No extra warnings and note should be given. 
                3. Don't apply css outside of 'story' class
                4. Only <div class='story'> class no complete html
                5. Output should not be inside ``` ```
                6. No Design related advices
                7. Don't apply css on body
                8. Use Hexcode for colors

                Expertise:
                1. Expert Story and Plot Writting
                2. Expert in Web Design and Know principles.

                Example output:
                <div class="story">
                    <h1>title</h1>
                    <p>
                        plot
                    </p>
                    <style>
                        .story subtags{

                        }
                        .story moresubtags{

                        }
                    </style>
                </div>
            """
        },{
        "role":"user",
        "content":f"Generate story about {additional_information} with {style} style",
    }])
    divInformmation = response.choices[0].message.content
    print("Generator")
    print(divInformmation)
    return divInformmation

def divExtractor(inforamtion):
    response = extractorai.chat.completions.create(model="phi3:latest",messages=[{
        "role":"system",
        "content":"""
            A Special Analysis Microservice returns string. it understands the content and extract <div> with story to return <div> tag along with content in response.
            Rules:
            - Remove any incomplete tags
            - Output shouldn't contain any warning message apart from story
            - Output only inlude relevant info no system warnings, errors, info 
            - It only returns <div> <style> <p> and <article> tags 
        """ 
    },
    {
        "role":"user",
        "content":f"{inforamtion}"
    }])
    divInfo = response.choices[0].message.content
    print("DIVINOF::: ")
    print(divInfo)
    return divInfo