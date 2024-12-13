from remembr.memory.memory import MemoryItem
from remembr.memory.milvus_memory import MilvusMemory

memory = MilvusMemory("test_collection", db_ip='127.0.0.1')

#memory.reset()

from remembr.memory.memory import MemoryItem

#memory_item = MemoryItem(
#    caption="I see a desk",
#    time=1.1,
#    position=[0.0, 0.0, 0.0],
#    theta=3.14
#)

#memory.insert(memory_item)

#from remembr.agents.non_agent import NonAgent

#agent = NonAgent(llm_type='command-r')

from remembr.agents.remembr_agent import ReMEmbRAgent

agent = ReMEmbRAgent(llm_type='command-r')
agent.set_memory(memory)

print ("start query")
response = agent.query("hey robot, go to the hallway")

print(response.position)
print(response.text)
