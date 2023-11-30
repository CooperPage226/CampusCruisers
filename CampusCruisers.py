from app import create_app, db
#from app.Model.models import Position, Research_field, Language, User
from flask_ckeditor import CKEditor, CKEditorField

app = create_app()
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
ckeditor = CKEditor(app)

#@app.shell_context_processor
#def make_shell_context():
    #return {'db': app.db, 'Position': Position, 'User': User}

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)