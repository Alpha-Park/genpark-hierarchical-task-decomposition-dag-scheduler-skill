from client import HierarchicalTaskDecompositionDAGSchedulerClient

def main():
    client = HierarchicalTaskDecompositionDAGSchedulerClient()
    res = client.schedule_task_dag()
    print('Task DAG Scheduler: ' + res['schedule_id'] + ' (Waves: ' + str(res['total_execution_waves']) + ')')
    print('Makespan: ' + str(res['estimated_makespan_sec']) + 's | Deadlock: ' + str(res['cyclic_deadlock_detected']))
    print('Visualization URL: ' + res['dag_visualization_url'])

if __name__ == '__main__':
    main()
