# Command Line Checklist
A command line program that allows for the creation, storage, and modification of simple checklists

# How to install

### Installing python and pip
<p> To install the required libraries, you need python: https://www.python.org/downloads/ <br>
Additionally, you must install pip: https://pip.pypa.io/en/stable/installing/
</p>

### Installing required libraries
<p> Download the files in this repository and place all of them in their own directory. Using the command line, navigate to the <br>
newly created directory and run the following in the command line (if you have python3, then you may have to use pip3 instead of pip):

`$ pip install -r requirements.txt`

</p>
  
# Running the program
<p> To run the program, simply navigate to the directory where the files from this repository are located, and use python to run <br>
checklist.py like so (if you have python3, simply change python to python3):

`$ python checklist.py`
</p>

# How to use
<p> When running the program for the first time, you should see 3 options like so: </p>
![Standard home menu. The program should look like this the first time it runs.](https://user-images.githubusercontent.com/85647626/122693714-9bc2cd00-d200-11eb-83af-56c4cd19fa0f.png)

<p> The 3 options you see are NOT items in the checklist, but default options that can be used to modify the list. <br>
To select options, press the number key corresponding to its position in the list of choices. To choose the option, press the enter key.
</p>

![A question that asks you to type in text](https://user-images.githubusercontent.com/85647626/122693978-8f8b3f80-d201-11eb-8ae7-3a226abb0977.png)
<p> Some choices will require you to input text, whether in the form of full words or a simple y/N (yes or no) response.
</p>

![A checklist with a couple of items](https://user-images.githubusercontent.com/85647626/122694080-e133ca00-d201-11eb-9173-2e85f2ef04ce.png)
<p> When the checklist has at least one item, they will be displayed below the 3 default options. Selecting any of these <br>
items will result in a yes or no prompt for whether or not to delete the item from the list.
</p>
