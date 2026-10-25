# Architecture Decision Records

Short, numbered records of decisions that shape GoCar. One file per
decision, named `NNN-short-title.md`. Use `000-template.md` as the
starting point.

| ADR | Title | Status | Phase |
|---|---|---|---|
| [001](001-godot-as-core.md) | Godot + GDScript as the simulation core | Accepted | 0b |
| [002](002-vehicle-collection.md) | World state holds a collection of vehicles | Accepted | 0b |

## When to write an ADR

- A decision changes an interface, schema, or contract.
- A decision is expensive to reverse.
- A decision resolves a trade-off future contributors will question.

Trivial implementation choices do not need an ADR.