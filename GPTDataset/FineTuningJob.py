from openai import OpenAI
client = OpenAI()

#UPLOAD FILES

def upload():
    upload = client.files.create(
      file=open(r"GPTDataset\SimplifyANDExpandMULTI-TURN-DATASET.json", "rb"),
      purpose="fine-tune"
    )
    return upload

def list():
    lst = client.files.list()
    return lst


def delete():
    delete = client.files.delete("file-2xyKS9xsSToiYoB1LC75r2")
    return delete

def create():
    client.files.list()
    #Create a fine-tuning job
    create = client.fine_tuning.jobs.create(
        training_file="file-2wthRj2XjG9g5nj9iFjLYp",
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::B0RlysA8"
    )
    return create

def event():
    event = client.fine_tuning.jobs.list_events(
      fine_tuning_job_id="ftjob-fL13NIbnrK9UdNRdb39kFvqN",
      limit = 20
    )
    return event

def retrieve():
    #Retrieve a data fine-tuning job
    retrieve = client.fine_tuning.jobs.retrieve("ftjob-fL13NIbnrK9UdNRdb39kFvqN")
    return retrieve


print(retrieve())
print("done")
