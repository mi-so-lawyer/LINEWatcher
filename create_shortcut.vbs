Set args = WScript.Arguments
Set shell = CreateObject("WScript.Shell")
Set shortcut = shell.CreateShortcut(args(1))
shortcut.TargetPath = args(0)
shortcut.WorkingDirectory = CreateObject("Scripting.FileSystemObject").GetParentFolderName(args(0))
shortcut.Save