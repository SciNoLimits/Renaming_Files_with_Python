# File Renamer

The File Renamer is a Python script that renames files in a specified folder. It can be useful for batch renaming multiple files with a common prefix or any desired naming convention.

## Usage

1. Make sure you have Python installed on your system.

2. Clone the repository or download the `file_renamer.py` file.

3. Open the `file_renamer.py` file in a text editor.

4. Modify the `folder` variable in the script to specify the path of the folder containing the files you want to rename. Replace `'YOUR_FILE_PATH/'` with the actual path to your folder.

5. Save the changes to the `file_renamer.py` file.

6. Open a terminal or command prompt and navigate to the directory where the `file_renamer.py` file is located.

7. Run the following command to execute the script:

   ```shell
   python file_renamer.py
   ```
8. The File Renamer is a Python script that iterates through each item in a specified folder and renames the files using a naming convention. By default, it    appends a numerical suffix (e.g., `filename0.jpg`, `filename1.jpg`, etc.) to the original file names.

9. The script will print the renaming process for each file unless commented out. If you want to visualize the process, uncomment the `print` statements by removing the leading `#` symbol.

10. Once the script finishes running, the files in the specified folder will be renamed according to the desired naming convention.

## Customization

You can customize the file naming convention by modifying the `dst` variable in the script. By default, it uses the original file name and appends a numerical suffix. You can change it to any naming convention that suits your needs.

## Dependencies

The File Renamer script does not have any external dependencies. It requires a Python interpreter (version 3 or above) to run.

## License

The File Renamer is released under the MIT License.

## Author

- Prajwal Dutta
- GitHub: [SciNoLimits](https://github.com/SciNoLimits)
