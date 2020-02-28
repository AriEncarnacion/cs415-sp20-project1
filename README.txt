Group: Ari Encarnacion, Vincent Valenzuela

Instructions given using unix based commands from mac terminal
Run the commands listed below for setup.

Instructions will be denoted by a "*". Interpret these instructions
depending on your specific device setup.

Specific commands will be denoted by a ">",
followed by the command to run.


Notes for commands will be beneath the command and indented.

    * Open a terminal on your LOCAL MACHINE
    	Packages will need to be installed. We were unable to figure out how to
    	install packages on blue with > pip install < as blue kept giving
    	permission denied errors.

    * Navigate to the directory /cs415-sp20-project1

    * run the command:
        > python3
            If python3 is not installed, please install python3.7.6
            preferably with > brew install < or use your install method of choice.

    * run the commands:
        > python3 pip -m install random2
            This will install the library random2.

        > python3 pip -m install matplotlib
            This will install the library matplotlib.

    * run the command:
        > mkdir generated_plots
            This will create a /generated_plots/ directory in which
            plots will be saved.

    * run the command:
        > python3 plot_mode.py
            This will execute a script that displays plots for all project tasks.
                If the script does not run due to a missing library please
                install that library using the command:
                    > python3 pip -m install <library name>

                When running plot mode, the script will display a single plot
                and then stop. To continue on to the next plot, close the current plot
                by clicking the "X" close window button on the plot gui.

                All plot values will be displayed in the console inside an array.

                *IMPORTANT* All generated plots will be stored in directory /generated_plots/.
                Plots are named by algorithm plotted followed by timestamp. This script does not
                reset the /generated_plots/ directory so ALL images will be saved. To clear this
                directory at any point, inside directory /project01_py/ run the command:
                    > rm generated_plots/*

    * run the command:
        > python3 user_test_mode.py
            This will execute the script to handle user testing input for all project tasks.
                If the script does not run due to a missing library please
                install that library using the command:
                    > python3 pip -m install <library name>

            Prompts for user input will be displayed in the terminal. Follow the prompt
            instructions to test the script. Script will terminate after each run.
