# plugcom

A minimal example of using a `uv` workspace to register subcommands via a plugin interface (using `pluggy`)

## Structure

The workspace members are placed under the `bin/` directory and configured as such in `pyproject.toml`.

### `plugcom-core`

Defines the base command `plg` and the plugin hooks (`hookspecs.py`). The `PlugcomGroup` is a `click.Group` that uses `pluggy`
features to call the hook functions and add commands.

We can add commands the typical way (e.g. `click.Group:add_command`) or via internal hook implementations (see `cli/run.py`).

The plugin interface is exposed through a setuptools entrypoint called "plugcom".

### plugcom-doit

The "external" plugin.

Hooks into the `plugcom-core` plugin interface with the following table in `pyproject.toml`

```toml
[project.entry-points.plugcom]
doit = "plugcom.doit"
```

The `plugcom.doit` module implements the `@plugcom_add_command` hookspec with a new `doit` subcommand.

#### Namespaces

Each package also defines a namespaced module beginning with `plugcom`. Though not necessary for this specific use case, it makes for nice imports:

- `from plugcom.core.cli import run`
- `from plugcom.doit ...`
