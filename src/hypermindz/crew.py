from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# from hypermindz.tools import MyCustomTool  # Example custom tool import
# from crewai_tools import SerperDevTool  # Example tool import

@CrewBase
class HypermindzCrew():
	"""Hypermindz crew template"""

	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"

	@agent
	def agent_one(self) -> Agent:
		return Agent(
			config=self.agents_config['agent_one'],
			# tools=[MyCustomTool,SerperDevTool()],
			verbose=True
		)

	@agent
	def agent_two(self) -> Agent:
		return Agent(
			config=self.agents_config['agent_two'],
			verbose=True
		)
	
	@agent
	def agent_three(self) -> Agent:
		return Agent(
			config=self.agents_config['agent_three'],
			verbose=True
		)

	@task
	def task_one(self) -> Task:
		return Task(
			config=self.tasks_config['task_one'],
			agent=self.agent_one(),
		)

	@task
	def task_two(self) -> Task:
		return Task(
			config=self.tasks_config['task_two'],
			agent=self.agent_two(),
		)
	
	@task
	def task_three(self) -> Task:
		return Task(
			config=self.tasks_config['task_last'],
			agent=self.agent_three(),
			output_file='output.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates a general crew setup"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical,
		)


