import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *

class N33t_Notepad(QMainWindow):
    def __init__(self):
        super(N33t_Notepad, self).__init__()
        self.path = None
        self.editor = QTextEdit()
        self.fontSizeBox = QSpinBox()
        font = QFont('Times', 15,  QFont.Normal)
        self.editor.setFont(font)
        self.setCentralWidget(self.editor)
        self.setGeometry(100, 100, 700, 500)
        self.create_menu_bar()
        self.create_status_bar()
        self.create_tool_bar()
        self.setWindowIcon(QIcon('app_icons/logo.png'))
        self.palette = QPalette()
        self.editor.setFontPointSize(24)

    def create_status_bar(self):
        # creating a status bar object
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        
    def create_menu_bar(self):
        # creating a file menu
        file_menu = self.menuBar().addMenu("&File")
        # creating actions to add in the file menu
        # creating a open file action
        open_file_action = QAction("Open file", self)
        # setting status tip
        open_file_action.setStatusTip("Open file")
        # adding action to the open file
        open_file_action.triggered.connect(self.file_open)
        # adding this to file menu
        file_menu.addAction(open_file_action)


        # similarly creating a save action
        save_file_action = QAction("Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)

 
        # similarly creating save action
        saveas_file_action = QAction("Save As", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)

 
        # for print action
        print_action = QAction("Print", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)

        # for exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # creating a edit menu bar
        edit_menu = self.menuBar().addMenu("&Edit")
  
        # undo action
        undo_action = QAction("Undo", self)
        # adding status tip
        undo_action.setStatusTip("Undo last change")
 
        # when triggered undo the editor
        undo_action.triggered.connect(self.editor.undo)
 
        # adding this to tool and menu bar
        
        edit_menu.addAction(undo_action)
 
        # redo action
        redo_action = QAction("Redo", self)
        redo_action.setStatusTip("Redo last change")
 
        # when triggered redo the editor
        redo_action.triggered.connect(self.editor.redo)
 
        # adding this to menu and tool bar
        edit_menu.addAction(redo_action)
 
        # cut action
        cut_action = QAction("Cut", self)
        cut_action.setStatusTip("Cut selected text")
 
        # when triggered cut the editor text
        cut_action.triggered.connect(self.editor.cut)
 
        # adding this to menu and tool bar
        edit_menu.addAction(cut_action)
 
        # copy action
        copy_action = QAction("Copy", self)
        copy_action.setStatusTip("Copy selected text")
 
        # when triggered copy the editor text
        copy_action.triggered.connect(self.editor.copy)
 
        # adding this to menu and tool bar
        edit_menu.addAction(copy_action)
 
        # paste action
        paste_action = QAction("Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
 
        # when triggered paste the copied text
        paste_action.triggered.connect(self.editor.paste)
 
        # adding this to menu and tool bar
        edit_menu.addAction(paste_action)
 
        # select all action
        select_action = QAction("Select all", self)
        select_action.setStatusTip("Select all text")
 
        # when this triggered select the whole text
        select_action.triggered.connect(self.editor.selectAll)

        # adding this to menu and tool bar
        edit_menu.addAction(select_action)

        # wrap action
        wrap_action = QAction("Wrap text to window", self)
        wrap_action.setStatusTip("Check to wrap text to window")
        # making it checkable
        wrap_action.setCheckable(True)
        # making it checked
        wrap_action.setChecked(True)
        # adding action
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        # adding it to edit menu not to the tool bar
        edit_menu.addAction(wrap_action)

        # # creating a edit menu bar
        # about_menu = self.menuBar().addMenu("&About")
        # # About Me
        # about_action = QAction("About Me", self)
        # about_action.setStatusTip("Informations about the author")
        # about_action.triggered.connect(self.launchPopup)
        # about_menu.addAction(about_action)
        # # Summary
        # sammary_action = QAction("Project", self)
        # sammary_action.setStatusTip("Informations about the project")
        # sammary_action.triggered.connect(self.launchPopup)
        # about_menu.addAction(sammary_action)
        
        



        # calling update title method
        self.update_title()
        # showing all the components
        self.show()
 
 

    def create_tool_bar(self):
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: white;")

        #Open File Button
        openBtn = QAction(QIcon('app_icons/open-file.png'), 'Open File', self)
        openBtn.triggered.connect(self.file_open)
        toolbar.addAction(openBtn)

        #Save Button
        saveBtn = QAction(QIcon('app_icons/save.png'), 'Save', self)
        saveBtn.triggered.connect(self.file_save)
        toolbar.addAction(saveBtn)

        #Print Button
        printBtn = QAction(QIcon('app_icons/print.png'), 'Print', self)
        printBtn.triggered.connect(self.file_print)
        toolbar.addAction(printBtn)

        #Undo Button
        undoBtn = QAction(QIcon('app_icons/undo.png'), 'Undo', self)
        undoBtn.triggered.connect(self.editor.undo)
        toolbar.addAction(undoBtn)

        #Redo Button
        redoBtn = QAction(QIcon('app_icons/redo.png'), 'Redo', self)
        redoBtn.triggered.connect(self.editor.redo)
        toolbar.addAction(redoBtn)

        #Copy Button
        copyBtn = QAction(QIcon('app_icons/copy.png'), 'Copy', self)
        copyBtn.triggered.connect(self.editor.copy)
        toolbar.addAction(copyBtn)

        #Paste Button
        pasteBtn = QAction(QIcon('app_icons/paste.png'), 'Paste', self)
        pasteBtn.triggered.connect(self.editor.paste)
        toolbar.addAction(pasteBtn)

        #Cut Button
        cutBtn = QAction(QIcon('app_icons/cut.png'), 'Cut', self)
        cutBtn.triggered.connect(self.editor.cut)
        toolbar.addAction(cutBtn)

        #Font Box
        self.fontBox = QComboBox(self)
        self.fontBox.addItems(["Courier Std","Hellentic Typewriter Regualr", "Helvetica", "Arial", "Times", "Monospace"])
        self.fontBox.activated.connect(self.setFont)
        toolbar.addWidget(self.fontBox)

        #Font Size Box
        self.fontSizeBox.setValue(15)
        self.fontSizeBox.valueChanged.connect(self.setFontSize)
        toolbar.addWidget(self.fontSizeBox)

        #Right Text Alignment Button
        rightAllign = QAction(QIcon('app_icons/right-align.png'), 'Right Allign', self)
        rightAllign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
        toolbar.addAction(rightAllign)

        #Left Text Alignment Button
        leftAllign = QAction(QIcon('app_icons/left-align.png'), 'Left Allign', self)
        leftAllign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
        toolbar.addAction(leftAllign)

        #Center Text Alignment Button
        centerAllign = QAction(QIcon('app_icons/center-align.png'), 'Center Allign', self)
        centerAllign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
        toolbar.addAction(centerAllign)


        #Bold Button
        boldBtn = QAction(QIcon('app_icons/bold.png'), 'Bold', self)
        boldBtn.triggered.connect(self.boldText)
        toolbar.addAction(boldBtn)

        #Italic Button
        italicBtn = QAction(QIcon('app_icons/italic.png'), 'Italic', self)
        italicBtn.triggered.connect(self.italicText)
        toolbar.addAction(italicBtn)

        #UnderLine Button
        undelineBtn = QAction(QIcon('app_icons/underline.png'), 'Undeline', self)
        undelineBtn.triggered.connect(self.underlineText)
        toolbar.addAction(undelineBtn)


        self.addToolBar(toolbar)
    
    #Method that is called when you press the fontSizeBox
    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)
    
    #Method that is called when you press the fontBox
    def setFont(self):
        font = self.fontBox.currentText()
        self.editor.setCurrentFont(QFont(font))
    
    #Check if text is italic or not
    def italicText(self):
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    #Check if text is undeline or not
    def underlineText(self):
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

    #Check if text is bold or not
    def boldText(self):
        if self.editor.fontWeight() == QFont.Bold:
            self.editor.setFontWeight(QFont.Normal)
        else:
           self.editor.setFontWeight(QFont.Bold)

    # action called by file open action
    def file_open(self):
        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
        # if path is true
        if path:
            # try opening path
            try:
                with open(path, 'rU') as f:
                    # read the file
                    text = f.read()
            # if some error occured
            except Exception as e:
                # show error using critical method
                self.dialog_critical(str(e))
            # else
            else:
                # update path value
                self.path = path
                # update the text
                self.editor.setPlainText(text)
                # update the title
                self.update_title()
 
    # action called by file save action
    def file_save(self):
        # if there is no save path
        if self.path is None:
            # call save as method
            return self.file_saveas()
        # else call save to path method
        self._save_to_path(self.path)
    
    #Save Function
    def file_save(self):
        # if there is no save path
        if self.path is None:
            # call save as method
            return self.file_saveas()
        # else call save to path method
        self._save_to_path(self.path)

    def file_saveas(self):
        # opening path
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")
        # if dialog is cancelled i.e no path is selected
        if not path:
            # return this method
            # i.e no action performed
            return
        # else call save to path method
        self._save_to_path(path)
    
    # save to path method
    def _save_to_path(self, path):
        # get the text
        text = self.editor.toPlainText()
        # try catch block
        try:
            # opening file to write
            with open(path, 'w') as f:
                # write text in the file
                f.write(text)
        # if error occurs
        except Exception as e:
            # show error using critical
            self.dialog_critical(str(e))
        # else do this
        else:
            # change path
            self.path = path
            # update the title
            self.update_title()
    # action called by print
    def file_print(self):
        # creating a QPrintDialog
        dlg = QPrintDialog()
        # if executed
        if dlg.exec_():
            # print the text
            self.editor.print_(dlg.printer())
 
    # update title method
    def update_title(self):
        # setting window title with prefix as file name
        # suffix aas PyQt5 Notepad
        self.setWindowTitle("%s - N33t Notepad - Version 0.01 - Author: Nikolaos Bikas" %(os.path.basename(self.path)if self.path else "Untitled"))
 
    # action called by edit toggle
    def edit_toggle_wrap(self):
        # chaining line wrap mode
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )

    # creating dialog critical method
    # to show errors
    def dialog_critical(self, s):
        # creating a QMessageBox object
        dlg = QMessageBox(self)
        # setting text to the dlg
        dlg.setText(s)
        # setting icon to it
        dlg.setIcon(QMessageBox.Critical)
        # showing it
        dlg.show()

    def launchPopup(self, item):
        pop = Popup(item.text(),self)
        pop.show()

class Popup(QDialog):
    def __int__(self, name, parent):
        super().__init__(parent)
        self.resize(600, 300)
        self.label = QLabel(name, self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = N33t_Notepad()
    windows.show()
    sys.exit(app.exec_())
