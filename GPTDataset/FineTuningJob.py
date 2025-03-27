from openai import OpenAI
client = OpenAI()

#UPLOAD FILES

def upload():
    upload = client.files.create(
      file=open(r"GPTDataset\QuestionnaireDATASET.json", "rb"),
      purpose="fine-tune"
    )
    return upload

def list():
    lst = client.files.list()
    return lst


def delete():
    delete = client.files.delete("file-4wBCTuGuaHTyTHKZxJzX8K")
    return delete

def create():
    client.files.list()
    #Create a fine-tuning job
    create = client.fine_tuning.jobs.create(
        training_file="file-8YY94x5RmwJjhyXE6mBeiz",
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::B4ichSCO"
    )
    return create

def event():
    event = client.fine_tuning.jobs.list_events(
      fine_tuning_job_id="ftjob-ytRmpOCvV8wh5N1h2tJAdrNE",
      limit = 20
    )
    return event

def retrieve():
    #Retrieve a data fine-tuning job
    retrieve = client.fine_tuning.jobs.retrieve("ftjob-ytRmpOCvV8wh5N1h2tJAdrNE")
    return retrieve

events = event()

for event in events:
    print(event, "\n")
print("done")
