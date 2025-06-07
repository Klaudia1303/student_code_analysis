# Feature extraction and error analysis module
import ast
import tempfile
import subprocess

def extract_features_from_code(code):
    """Estrae caratteristiche sintattiche dal codice Python."""
    tree = ast.parse(code)
    return {
        'num_nodes': len(list(ast.walk(tree))),
        'num_functions': sum(isinstance(n, ast.FunctionDef) for n in ast.walk(tree)),
        'num_loops': sum(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree)),
        'num_if': sum(isinstance(n, ast.If) for n in ast.walk(tree)),
        'num_assign': sum(isinstance(n, ast.Assign) for n in ast.walk(tree)),
        'num_calls': sum(isinstance(n, ast.Call) for n in ast.walk(tree)),
        'avg_func_length': avg_function_length(tree)
    }

def avg_function_length(tree):
    """Calcola la lunghezza media delle funzioni nel codice."""
    lengths = [len(n.body) for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    return sum(lengths) / len(lengths) if lengths else 0

def check_code_errors(code):
    """Controlla errori di sintassi e runtime nel codice."""
    syntax_error = 0
    runtime_error = 0
    error_type = ""

    # Controllo di sintassi
    try:
        compile(code, "<string>", "exec")
    except SyntaxError:
        syntax_error = 1
        error_type = "SyntaxError"
        return syntax_error, runtime_error, error_type

    # Controllo di esecuzione
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as tmp:
            tmp.write(code)
            tmp.flush()
            result = subprocess.run(
                ["python", tmp.name],
                capture_output=True,
                text=True,
                timeout=3
            )
            if result.returncode != 0:
                runtime_error = 1
                error_type = result.stderr.split(":")[0] if result.stderr else "RuntimeError"
    except Exception as e:
        runtime_error = 1
        error_type = str(e).split(":")[0]

    return syntax_error, runtime_error, error_type
