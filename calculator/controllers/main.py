"""
Main module.
It has all the operations available for this app.
"""
#!/usr/bin/env python
from flask import Blueprint, session, abort, jsonify, request
from calculator.models import db, PersistedSession, Operation
from calculator.calculator import evaluator

main = Blueprint('main', __name__)

@main.route('/operations', methods=["GET"])
def list_operations():
    """
    Lists current operations in session.
    """
    if 'operations' in session:
        return jsonify({'Operations:': session['operations']})

    return jsonify({'Operations:': []})


@main.route('/operations', methods=["POST"])
def add_operation():
    """
    Adds an operation to current session.
    """
    if not request.form.get('input', ''):
        return abort(400, 'No input parameter.')

    if 'operations' not in session:
        session['operations'] = []

    try:
        output = evaluator(request.form['input'])
    except Exception as err:
        return abort(500, str(err))

    temp = session['operations']
    session.pop('operations')
    temp += [{'input' : request.form['input'], 'output' : output}]
    session['operations'] = temp
    return jsonify({'output': output}), 200

@main.route('/operations', methods=["DELETE"])
def clean_operations():
    """
    Clears operations for current session.
    """
    if 'operations' in session:
        session.pop('operations')

    return jsonify({'message': "Operation for session cleaned."})

@main.route("/sessions", methods=["GET"])
def list_sessions():
    """
    List all available sessions.
    """
    try:
        sessions = PersistedSession.query.all()

        if not sessions:
            return jsonify({'Sessions': []})

        return jsonify({'Sessions': [i.serialize() for i in sessions]})

    except Exception as err:
        return abort(500, "Error listing sessions: %s" % str(err))


@main.route("/sessions/<string:session_name>", methods=["GET"])
def get_session(session_name):
    """
    Get a session. It only return the dession description.
    It does not replace current operations.
    """
    try:
        s = PersistedSession.query.filter_by(name=session_name).first()

        if not s:
            return abort(400, "Session name = %s not found." % session_name)

        query = Operation.query.filter_by(session_id=s.id).all()

        operations = []
        for operation in query:
            operations.append("Input: %s, Output: %s" %
                              (operation.input, operation.output))

        return jsonify({'session': s.serialize()})

    except Exception as e:
        return abort(500, "Error getting session: %s" % str(e))

@main.route("/sessions/<string:session_name>", methods=["POST"])
def save_session(session_name):
    """
    Saves a session.
    It works if the current session has operations to save.
    If session name already exists in the database It returns an abort response.
    """
    if 'operations' in session:
        s = PersistedSession.query.filter_by(name=session_name).first()

        if s:
            # Think about update session functionality.
            return abort(400, "The session name '%s' already exists.\
                               Please use another session name \
                               or delete the session using that name. "
                         % session_name)

        try:
            s = PersistedSession(session_name)
            db.session.add(s)

            for operation in session['operations']:
                c = Operation(session = s,
                              input = operation['input'],
                              output = operation['output'])
                db.session.add(c)

            db.session.commit()
            session.pop('operations', None)

            return jsonify({'message': "Session saved. id: %s, name: %s" % (s.id, s.name)}), 200

        except Exception as err:
            return abort(500, "Error saving session: %s" % str(err))

    return abort(400, "Can't save: Empty Session")

@main.route("/sessions/<string:session_name>", methods=["DELETE"])
def delete_session(session_name):
    """
    Deletes a session.
    Delete operations related to that session.
    """
    try:
        s = PersistedSession.query.filter_by(name=session_name).first()

        if not s:
            return abort(400, "Session name = %s not found." % session_name)

        db.session.delete(s)
        db.session.commit()
        return jsonify({'message': "Session deleted."})

    except Exception as err:
        return abort(500, "Error deleting session: %s" % srt(err))
