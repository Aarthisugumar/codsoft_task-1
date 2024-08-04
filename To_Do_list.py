import argparse
l = []
status = []
def add(task):
    l.append(task)
    print("Task {} added".format(len(l)))

def update(index, task_update):
    l[index] = task_update
    print("Task {} updated".format(index))

def view():
    #for i in range(len(l)):
        #if status[i] == "completed":
            #print("ID: {}, Description: {}, Status: completed".format(i, l[i]))
        else:
            status.append("incompleted")
            print("ID: {}, Description: {}, Status: incompleted".format(i, l[i]))

def delete(index):
    l.pop(index)
    print("Task {} deleted".format(index))

def complete(index):
    if index < len(status):
        status[index] = "completed"
    else:
        status.insert(index, "completed")
    print("Task {} completed".format(index))

def main():
    parser = argparse.ArgumentParser(description="Task manager")
    parser.add_argument('action', choices=['add', 'update', 'view', 'delete', 'complete'], help="Action to be performed")
    parser.add_argument('--task', help="Task description for 'add' and 'update' actions")
    parser.add_argument('--index', type=int, help="Task index for 'update', 'delete', and 'complete' actions")

    args = parser.parse_args()

    if args.action == 'add':
        if args.task:
            add(args.task)
        else:
            print("Task description is required for adding a task.")
    elif args.action == 'update':
        if args.index is not None and args.task:
            update(args.index, args.task)
        else:
            print("Both task index and description are required for updating a task.")
    elif args.action == 'view':
        view()
    elif args.action == 'delete':
        if args.index is not None:
            delete(args.index)
        else:
            print("Task index is required for deleting a task.")
    elif args.action == 'complete':
        if args.index is not None:
            complete(args.index)
        else:
            print("Task index is required for marking a task as completed.")

if __name__ == "__main__":
    main()
