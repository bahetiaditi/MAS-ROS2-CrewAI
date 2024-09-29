from crewai import Task
import time

import sys
sys.path.append("/home/nachiketa/dup_auto_ass1/src")
from common_interfaces.src.logger_config import ret_logger

class EscortToEntranceTask(Task):
    def __init__(self, agent):
        super().__init__(
            description='Escort visitor from the host back to the campus entrance.',
            expected_output='Visitor successfully escorted back to the campus entrance.',
            agent=agent
        )

        self._logger = ret_logger()

    def execute(self, inputs):
        visitor_id = inputs['visitor_id']
        building_id = inputs['building_id']
        room = inputs['room']
        navigation_path = inputs['navigation_path']
        agent_id = inputs['agent_id']
        meeting_time = inputs['meeting_time']

        self._logger.info(f"{agent_id} is waiting for meeting to finish")
        time.sleep(int(meeting_time))

        # Phase 1: Guide visitor back to the building entrance
        self.agent.tools[3].run(agent_id, visitor_id, building_id, navigation_path)

        return True