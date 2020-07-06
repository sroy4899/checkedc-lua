# Checked C Lua Conversion
This repository is dedicated to the testing of the Checked-C conversion tool available [here](https://github.com/plum-umd/checkedc-clang/tree/BigRefactor). 

This repository contains several branches. This branch (**master**) will have C code and relevant documentation.   

[Baseline](https://github.com/sroy4899/checkedc-lua/tree/baseline) represents this same C Code, but refactored in order to mimic the structure of [a similar repo for testing vsftpd](https://github.com/plum-umd/checkedc-eval-vsftpd/blob/re-port/README.md). It includes scripts for running the conversion tool and replacing the converted files. 

[Sane-baseline](https://github.com/sroy4899/checkedc-lua/tree/sane-baseline) represents code from **Baseline** that has been modified in order to make conversion work. (EX. pruning features that are not yet supported by the tool that are making it crash, etc.). As the tool evolves and these features are supported, changes in **Sane-baseline** will be reverted/modified. 

[Baseline-converted](https://github.com/sroy4899/checkedc-lua/tree/baseline-converted) represents code from **Baseline** that has been fully converted with the latest changes from the conversion tool. Commits to this branch are hashed by the relevant commit from the tool. Conversion on this branch is run without `-alltypes`, so will only support `_Ptr` conversions. 

Similarly, [Sane-baseline-converted](https://github.com/sroy4899/checkedc-lua/tree/sane-baseline-converted) represents code from **Sane-baseline** that has been converterted with the `-alltypes` flag enabled, thereby supporting `_Array_ptr`, `_Nt_array_ptr`, and `_Checked` annotations. 

In order to test lua, please make sure that you have the package `readline` installed in order to prevent errors. On a linux machine, this can be achieved with 
```
sudo apt-get install libreadline-dev
```
For OSX: 
```
brew install readline
```

To get started, simply run:
```
python3 run.py
``` 
It is recommended you open up a separate tab in order to copy paste file locations that the script will prompt you for. After putting in the file locations, the script will automatically: 
1) checkout baseline, update scripts with your information, run, compile, and diff the tool against baseline-converted 
2) checkout sane-baseline, update scripts with your information, run and compile the tool
3) reset the changes to sane-baseline and run the tool with alltypes and diff the tool 

After each of these three "phases", the script will output relevant information about the number of diffs, etc. 
