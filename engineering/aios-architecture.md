# AIOS Architecture

[English](./aios-architecture.md) | [简体中文](./aios-architecture.zh-CN.md)

> Role: realize "reality — finite system — six-dimensional boundary — sufficiency — exploration/decision — action chain" in a long-running autonomous AI system. AIOS is an application of the framework, not its source.

## 1. From framework to runtime

AIOS is itself a finite system. It does not implement "reality" as a total ontology and does not claim that personal-world, databases, models, or knowledge graphs contain the whole world.

The runtime needs to preserve:

- **current boundary**: distinction, relation, causality, temporality, possibility, value;
- **epistemic status**: provenance, evidence, unknowns, disputes, versions, freshness;
- **sufficiency basis**: why the current transition is sufficient now;
- **exploration / decision state**: reopen when insufficient, choose when sufficient;
- **action chain**: decision, authorization, execution, real-world effect, observation, verification, outcome, recovery, reopening.

The six dimensions do not map to six services. They are semantic requirements that can be carried by different domain objects.

## 2. Long-running loop

```text
┌────────────────────────────────────┐
│ AIOS: finite system                │
│                                    │
│ observe / distinguish boundary     │
│ → sufficiency                      │
│ → explore or decide                │
│ → authorize → execute              │
│ → observe → verify → reconcile     │
└──────────────┬─────────────────────┘
               │ bounded real-world effect
               ▼
            ┌─────────┐
            │ Reality │
            └──┬──────┘
               │ authoritative readback / evidence / unknown
               └────────────────────► AIOS
```

Normal operation does not depend on a human being present. Reality-side feedback can reopen any part of the current boundary.

## 3. Temporary external intervention

```text
Human
  │ query / request / required approval
  ▼
Existing Agent product
(short-lived session)
  │ authoritative inspection / explanation /
  │ bounded authorized repair / verification
  ▼
AIOS machine boundary ─────────────► Reality
  │
  └── report verified state, then disconnect
```

The external Agent:

- is not part of the AIOS runtime;
- does not own durable state, responsibility, or authority;
- is not the owner of personal-world or domain truth;
- does not pause autonomous AIOS operation when its session ends.

`human present != system operation requires human`

`external Agent explanation != authoritative state`

`external Agent repair != successful recovery`

`successful recovery = authoritative state + reality-side readback + required verification`

API / CLI are machine integration and maintenance boundaries, not the primary human management surface.

## 4. Architectural regions

```text
┌────────────────────────────────────────────────────────────────┐
│ AIOS — long-running autonomous finite system                   │
│                                                                │
│ personal-world ──purpose-limited context──► internal Agent     │
│      ▲                                      / executor          │
│      │ provenance / revision                    │               │
│      └────────────────────────────────────────► domain admission│
│                                                 │              │
│ semantic-language / world-runtime / domain controllers         │
│ boundary / sufficiency / responsibility / authority /          │
│ action chain / recovery                                        │
└─────────────────────────┬──────────────────────────────────────┘
                          │
                          ▼
                        Reality
     external systems / source / build / deploy / traffic /
     infrastructure / organizational systems

Out of band, only when needed:
Human ⇄ short-lived Agent product ⇄ AIOS machine boundary
```

A container is a deployment boundary, not a durable semantic owner. Internal Agents, executors, model providers, monitoring systems, and external clients remain replaceable.

## 5. Repository and component ownership

| Component | Ownership |
| --- | --- |
| guide | framework, six dimensions, sufficiency, exploration/decision, action chain, engineering invariants |
| aios | AIOS source monorepo |
| semantic-language | stable cross-domain role vocabulary, references, normalization, non-substitution |
| personal-world | durable personal facts, preferences, relations, resource refs, provenance, revision, freshness, privacy, purpose-limited context |
| world-runtime | durable agency, responsibility, decisions, sufficiency basis, authorization, execution identity, recovery, reconciliation, history |
| control-plane | operational incidents, diagnosis, repair, monitoring, runtime providers, result evidence |
| administrative-orchestrator | administrative cases, obligations, governance basis, administrative effects, outcomes, completion semantics |
| autonomous-development | software requirements, source, build, test, deploy, canary, promotion, rollback, release semantics |
| Agent / executor | replaceable cognitive or engineering implementation |
| model provider / router | replaceable model access |
| external provider | real-world effects and authoritative external state |

Directories can own independent semantics without becoming separate Git repositories.

## 6. semantic-language: cross-domain constitution

semantic-language stays small and stable, expressing only cross-domain role distinctions that recur and whose collapse causes concrete correctness failure.

At minimum preserve:

```text
reality != current representation
distinguishable range != distinguished range
default distinction != sufficient distinction
relation != causality
possible != reachable != controllable != callable
question candidate != sufficiently established question
interpretive sufficiency != specified sufficiency
specified rule satisfied != rule applicable / current / authoritative
evidence != belief
observation != claim
claim != current sufficiently established state
intent candidate != confirmed human intent
human approval action != decision
decision != authorization
authentication != representation
representation != state-transition authority
personal context != execution permission
real-world effect != outcome
provider success != verified reality
projection != authoritative state
historically valid != currently sufficient
interpretation != reality
```

A stable semantic distinction does not automatically require a universal payload, durable entity, table, or service.

## 7. personal-world: personal continuity

personal-world owns a person's durable, evolving, provenance-bearing context accepted through proportionate sufficiency judgments.

```text
source
→ observation
→ claim
→ sufficiency
→ personal record revision
→ current lineage head
→ purpose-limited context projection
→ Agent / authorized consumer
```

Public personal record types may include:

```text
personal fact
preference
relation
resource link
```

personal-world does not own:

```text
decision
authorization
responsibility
run
real-world effect
domain outcome
provider execution
domain lifecycle
model-private memory
```

Model inference does not automatically become accepted personal truth. Domain projections do not transfer domain ownership. Context projections are not new authoritative personal state.

## 8. Cognitive execution

Cognitive execution is a replaceable boundary:

```text
domain trigger / authorized request
+ purpose-limited personal context
+ domain state
+ runtime constraints
→ Agent / executor
→ boundary review
→ exploration when needed
→ problem / task sufficiency
→ analysis / proposal / implementation candidate / test / review
```

Executor output remains candidate distinctions, evidence, explanations, proposals, implementations, or review results. A newly generated framing does not automatically obtain domain admission.

Model selection and routing are transport / configuration matters; they do not expand authority, real-world effect scope, or durable ownership.

## 9. world-runtime: autonomous continuity

world-runtime sits between sufficiently established work triggers and domain realization:

```text
sufficient work trigger / authorized request
        ↓
governed autonomous capability
        ↓
world-runtime
        ↓
bounded domain realization
        ↓
Reality
```

world-runtime may own:

```text
identity
epistemic-basis refs
responsibility
decision
authorization warrant / authorization
policy
sufficiency basis
work / run
execution identity
provider-attempt identity
reconciliation
recovery
history lineage
```

It does not own personal preferences, interface session state, software release semantics, administrative completion semantics, or provider-specific business semantics.

Domain controllers define domain completion and result meanings.

## 10. Authority path

```text
authenticated actor
→ representation
→ intent / proposal
→ decision
→ authorization warrant / authorization
→ runtime state-transition authority
→ domain execution authorization
→ durable real-world effect identity
→ provider dispatch
→ Reality
```

An earlier position cannot substitute for a later one.

Knowing a resource does not create permission. Representing a principal does not automatically create transition authority. Transition authority does not automatically create every real-world effect permission. Execution authority does not prove domain outcome.

## 11. Evidence and feedback path

```text
Reality
→ observation
→ evidence
→ domain interpretation
→ outcome / unknown candidate
→ sufficiency
→ responsibility evaluation
→ current autonomous state
```

Evidence must remain traceable to sources. Changes in current sufficiency do not rewrite historical evidence. Material basis changes trigger revalidation.

## 12. control-plane

```text
monitoring signal
→ authenticated entry
→ runtime responsibility + domain assignment
→ bounded diagnosis
→ repair-plan sufficiency
→ domain work / run
→ runtime provider
→ reality-side observation
→ repair verification
→ domain report
→ runtime responsibility evaluation / release
```

Diagnosis is not authority. Provider success is not target recovery. Operational completion requires domain evidence.

## 13. administrative-orchestrator

```text
organizational request / evidence
→ administrative case / facts / rules / obligations
→ governance basis
→ administrative execution authorization
→ runtime responsibility / work / permission
→ external administrative system
→ independent readback
→ confirmed outcome
→ completion evaluation
→ runtime responsibility evaluation
```

Rule or approval satisfaction is not runtime authorization. An administrative effect record is not external reality. Case completion does not automatically discharge responsibility.

## 14. autonomous-development

```text
sufficient development goal / admitted request
→ development request
→ personal-world context projection
→ requirements analysis
→ change proposal
→ isolated implementation
→ deterministic verification + independent review
→ immutable build
→ candidate deployment
→ offline evaluation
→ canary
→ promotion or rollback
→ post-promotion observation
→ release version
```

autonomous-development owns:

```text
development goal
product-goal revision
development request
requirements analysis
change proposal
worktree / source semantics
verification gates
build artifact identity
deployment state
traffic exposure
feedback attribution
canary lifecycle
promotion
rollback
release version
```

`Git commit != release version`

`tests pass != promotion authority`

`deployment healthy != product improved`

`canary complete != release finally confirmed`

personal-world inputs bind revisions. Personal context changes do not rewrite historical analysis, but can invalidate the current sufficiency of old analysis.

## 15. Reality return path

Every consequential path contains a return path:

```text
Reality
→ observation / provider receipt / external state
→ domain evidence
→ real-world effect / outcome / unknown
→ world-runtime reconciliation and sufficiency
→ responsibility evaluation
→ current autonomous state / next cycle
```

Only when an exception needs human attention is this state projected through a short-lived Agent.

Provider acknowledgment alone cannot terminate the loop. Transport ambiguity remains unknown. Where supported, independent readback confirms reality.

## 16. Three durable continuities

```text
personal continuity = personal-world
autonomous continuity = world-runtime
domain continuity = domain controller
```

semantic-language preserves role distinctions across the three.

External Agent projections are not a fourth durable authority store.

Replacing internal Agents / executors must not replace durable continuity; disconnecting an external client must not stop AIOS; domain controllers can evolve without moving specialist lifecycle semantics into world-runtime; world-runtime can restart without losing durable autonomous state.

## 17. Placement rules

Promote a role distinction into semantic-language only when at least three materially different domains need the same stable cross-domain distinction and collapsing it causes concrete correctness failure. Promotion adds only the role distinction, not domain payloads or lifecycle.

New durable cross-domain autonomous invariants go to world-runtime.

Personal facts, preferences, relations, resource refs, and context lineage go to personal-world.

Specialist lifecycle belongs to domain controllers.

Provider-specific implementation stays under the owning domain.

Agents / executors and model routing remain replaceable and do not become durable state owners by default.

## 18. Extension topology

New executor:

```text
autonomous work / domain request
→ executor selection
  ├─ Agent adapter
  ├─ engineering executor
  └─ specialized executor
```

New domain:

```text
world-runtime
  ├─ control-plane
  ├─ administrative-orchestrator
  ├─ autonomous-development
  └─ future domains
```

New provider:

```text
domain controller
  ├─ API
  ├─ app
  ├─ device
  ├─ infrastructure
  ├─ human
  └─ robot
```

New capability does not automatically require new runtime semantics. A stronger model does not create durable authority. A new domain does not imply a universal domain ontology.

## 19. Stable architecture

```text
guide
  reality / finite system
  six-dimensional boundary
  sufficiency
  exploration / decision
  action chain
       │
       ▼
aios/semantic-language
  cross-domain semantic constitution

AIOS
  personal-world ──► internal Agent / executor
         ▲                     │
         │                     ▼
         └────────────── domain admission
                               │
                               ▼
                         world-runtime
                               │
             ┌─────────────────┼──────────────────┐
             ▼                 ▼                  ▼
        control-plane   administrative      autonomous-
                         orchestrator        development
             │                 │                  │
             └─────────────────┼──────────────────┘
                               ▼
                             Reality
                               │
          evidence / readback / result / unknown
                               └──────────────► AIOS

Out of band:
Human → short-lived Agent → AIOS machine boundary
        inspect / explain / authorized repair / verify / report / disconnect
```

AIOS stability comes from durable semantic ownership, reality-side return paths, and the action chain rather than dependence on any particular Agent, model provider, router, or interactive client.
