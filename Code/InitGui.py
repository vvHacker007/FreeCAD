class MyWorkbench (Workbench):
    
    MenuText = "New Features"

    def Initialize(self):
        import three_point_para
        import Mid_Point_Line
        commandslist = ["para","midpoint_line"]
        self.appendToolbar("Features", commandslist)

Gui.addWorkbench(MyWorkbench())