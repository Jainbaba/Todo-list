from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    '''Method to handle 404 Error
    
    Args:
        error: This is the error raised when there is a incorrect endpoint.
    Returns:
        json['error']: Endpoint not found.
    '''
    return {'error': 'Endpoint not found.',}, 404

@errors.app_errorhandler(405)
def error_405(error):
    '''Method to handle 405 Error
    
    Args:
        error: This is the error raised when there is a incorrect method.
    Returns:
        json['error']: Method not allowed.
    '''
    return {'error': 'Method not allowed.',}, 405

@errors.app_errorhandler(500)
def error_500(error):
    '''Method to handle 505 Error
    
    Args:
        error: This is the error raised when is a issue with the applcation.
    Returns:
        json['error']: Internal server error.
    '''
    return {'error': 'Internal server error.',}, 500
