from master.master import Master

if __name__ == "__main__":
    with (Master(1, "127.0.0.1:20000") as master):
        # Creates outstation association, adds polling, enables master channel, and runs main input loop
        master.run(1024)
