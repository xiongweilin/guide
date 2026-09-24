# Personal AI OS Architecture

## System shape

```text
Human / Operator
  │
  │ intent / correction / approval / intervention
  ▼
Operator Interface
(API / CLI / automation adapter)
  │
  ├──────────────► Personal World
  │                  │
  │                  │ purpose-limited context
  │                  │ provenance / revision / freshness
  │                  ▼
  │              Agent / Executor
  │                  │
  │                  │ analysis / candidate / evidence request
  │                  ▼
  └──────────────► Domain Controller
                     │
                     │ governed agency request
                     ▼
                 World Runtime
                     │
                     │ authority / responsibility / execution identity
                     │ effect admission / recovery / reconciliation
                     ▼
                 Domain Controller
                     │
                     │ provider-specific execution
                     ▼
          APIs / Apps / Git / Infrastructure /
             Devices / External Systems / Humans
                     │
                     ▼
                   Reality
                     │
                     │ observation / read-back / telemetry / receipts
                     ▼
                 Domain Controller
                     │
                     │ evidence / outcome / unknown
                     ▼
                 World Runtime
                     │
                     │ qualification / responsibility assessment
                     │ decision / reconciliation / historical continuity
                     ▼
             Operator Interface
                     │
                     │ explanation / projection / remaining uncertainty
                     ▼
                 Human / Operator
```

`semantic-language` supplies cross-domain semantic distinctions across the architecture.

`guide` holds doctrine, qualification rules, failure distinctions, and architectural invariants.

Agent implementations, model providers, model-routing gateways, monitoring systems, and deployment runtimes are replaceable integrations. None becomes a durable semantic owner merely because a deployment uses it.

## Architectural regions

```text
┌──────────────────────────────────────────────────────────────────────┐
│ HUMAN / OPERATOR BOUNDARY                                            │
│                                                                      │
│ Human ⇄ API / CLI / automation adapter                               │
│ intent / clarification / approval / intervention / projection         │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PERSONAL CONTEXT AND COGNITION                                       │
│                                                                      │
│ Personal World ──purpose-limited projection──► Agent / Executor       │
│      ▲                                      │                        │
│      │ provenance / correction              │ analysis / candidate  │
│      │                                      ▼                        │
│      └──────────────────────────── Agency / Domain admission          │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ DURABLE AGENCY                                                       │
│                                                                      │
│ semantic-language                                                    │
│ world-runtime                                                        │
│                                                                      │
│ meaning / identity / responsibility / authority / decision /         │
│ strategy / qualification / execution identity / recovery / history   │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ DOMAIN REALIZATION                                                   │
│                                                                      │
│ control-plane                                                        │
│ administrative-orchestrator                                          │
│ autonomous-development                                               │
│                                                                      │
│ domain lifecycle / professional semantics / providers / read-back    │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ REALITY                                                              │
│                                                                      │
│ external systems / source repositories / builds / deployments /      │
│ traffic / infrastructure / organizational systems / human actions    │
└──────────────────────────────────────────────────────────────────────┘
```

The architecture does not require a graphical UI. Human/operator interaction is a replaceable boundary and may be exposed through API, CLI, or another adapter.

## Repository topology

| Repository / component | Ownership |
| --- | --- |
| [guide](https://github.com/xiongweilin/guide) | doctrine, qualification, distinctions, architectural invariants |
| [aios](https://github.com/xiongweilin/aios) | monorepo and Git owner for AIOS source components |
| [semantic-language](https://github.com/xiongweilin/aios/tree/main/semantic-language) | cross-domain meanings and non-substitution rules |
| [personal-world](https://github.com/xiongweilin/aios/tree/main/personal-world) | durable personal facts, preferences, relationships, resource links, provenance, revisions, freshness, privacy boundaries, purpose-limited context |
| [world-runtime](https://github.com/xiongweilin/aios/tree/main/world-runtime) | durable agency state, responsibility, authority, decisions, qualification, execution identity, recovery, reconciliation, history |
| [control-plane](https://github.com/xiongweilin/aios/tree/main/control-plane) | operational incidents, bounded repair, monitoring, operational providers, operational outcome evidence |
| [administrative-orchestrator](https://github.com/xiongweilin/aios/tree/main/administrative-orchestrator) | administrative cases, obligations, governance basis, administrative effects, business outcome and completion semantics |
| [autonomous-development](https://github.com/xiongweilin/aios/tree/main/autonomous-development) | software-development lifecycle, requirements, source/build/test/deploy/canary/promotion/rollback semantics |
| Agent / executor adapters | replaceable cognition or engineering execution implementations |
| Model providers / routing adapters | replaceable model access and protocol transport |
| Providers and external systems | concrete effects and authoritative external state |
| Reality | the state that execution attempts to change and observation attempts to establish |

A component directory may remain a distinct semantic owner without being a distinct Git repository.

## Cross-cutting semantic constitution

`semantic-language` remains small and cross-domain.

```text
Evidence != Belief
Observation != Claim
Claim != current qualified state
IntentCandidate != confirmed human intent
HumanApprovalGesture != Decision
Decision != Authorization
Authentication != Representation
Representation != transition authority
Personal context != execution authority
Effect != Outcome
Provider success != verified reality
Projection != authoritative state
Historical validity != current qualification
Explanation != reality
```

Domain-specific meanings remain domain-owned.

Runtime lifecycle meanings remain Runtime-owned.

Personal meanings remain Personal World-owned.

Human interaction/session state belongs to the active operator-interface layer and does not become durable authority.

## Human boundary

The Human ⇄ Agency boundary is interface-neutral.

```text
Human input
  ↓
IntentCandidate
  ↓
context-limited interpretation
  ↓
Proposal / Development requirement candidate
  ↓
HumanApprovalGesture / rejection / intervention
  ↓
authoritative owner admission
```

Operator-interface state is limited to ephemeral interaction state and projections of authoritative owners.

The interface does not own durable authority, durable responsibility, Personal World truth, domain lifecycle truth, domain outcome, model routing, or agent execution.

A command changes state only through the authoritative owner.

A projection remains read-only and disposable.

Ambiguous command transport remains `pending-reconciliation` until authoritative read-back resolves it.

## Personal continuity

`personal-world` owns one person's durable evolving context.

```text
Source
  ↓
Observation
  ↓
Claim
  ↓
Qualification
  ↓
Personal Record Revision
  ↓
Current lineage head
  ↓
Purpose-limited ContextProjection
  ↓
Agent / authorized consumer
```

Public personal record kinds remain:

```text
PersonalFact
Preference
Relationship
ResourceLink
```

Personal World does not own:

```text
Decision
Authorization
Mandate
Responsibility
Work
Run
Effect
Outcome
provider execution
domain lifecycle
model-private memory
```

A model inference does not become accepted personal truth by itself.

A domain projection does not transfer domain ownership into Personal World.

A ContextProjection does not become canonical Personal World state.

## Cognitive execution

Cognitive execution is a replaceable boundary.

```text
Human intent
  +
Purpose-limited Personal World context
  +
Domain state
  +
Runtime constraints
  ↓
Agent / Executor
  ↓
analysis / proposal / implementation candidate / test / review
```

The executor does not own durable authority, durable responsibility, Personal World truth, or domain completion.

Executor output remains evidence, interpretation, proposal, implementation candidate, or review result according to the receiving boundary.

Model selection and model routing are transport/configuration concerns beneath the executor boundary. They do not widen authority or effect scope, and changing them does not replace Personal World, Runtime state, Domain state, responsibility, or history.

## Durable agency

`world-runtime` is the agency continuity membrane between interpreted intent and domain realization.

```text
Human-side interpretation
        │
        ▼
   governed agency
        │
        ▼
   WORLD RUNTIME
        │
        ▼
 bounded realization
        │
        ▼
    Reality-side
```

Runtime owns generic durable agency primitives:

```text
identity
epistemic references
responsibility
decision
mandate
authorization
strategy
qualification
Work / Run
execution identity
provider-attempt identity
reconciliation
recovery
historical lineage
```

Runtime does not own:

```text
personal facts or preferences
UI interaction state
model selection policy
software release semantics
administrative completion semantics
incident-repair semantics
provider-specific business semantics
```

Runtime governs whether an agency transition or reality-bound effect may proceed.

Domain Controllers determine what domain completion and domain outcome mean.

## Domain realization

### Control Plane

`control-plane` owns operational reality.

```text
monitoring signal
  ↓
authenticated ingress
  ↓
Runtime Responsibility + DomainAssignment
  ↓
bounded diagnosis
  ↓
RepairClosure
  ↓
DomainWork / DomainRun
  ↓
operational provider
  ↓
reality observation
  ↓
RepairRevision
  ↓
DomainReport
  ↓
Runtime assessment / Decision / discharge
```

Operational diagnosis is not authority.

Provider success is not target recovery.

Operational completion requires domain evidence.

### Administrative

`administrative-orchestrator` owns administrative reality.

```text
organizational request / evidence
  ↓
Administrative case / facts / policy / obligations
  ↓
GovernanceBasis
  ↓
Administrative ExecutionAuthorization
  ↓
Runtime Responsibility / Work / Run / authority
  ↓
external administrative system
  ↓
independent read-back
  ↓
ConfirmedOutcome
  ↓
CompletionAssessment
  ↓
Runtime responsibility assessment
```

Administrative approval satisfaction is not Runtime Authorization.

An Administrative EffectRecord is not external reality.

Case completion is not automatic Runtime responsibility discharge.

### Autonomous Development

`autonomous-development` owns software-development reality.

```text
Human requirement
  ↓
DevelopmentRequest
  ↓
Personal World context projection
  ↓
engineering executor requirement analysis
  ↓
ChangeProposal
  ↓
isolated implementation
  ↓
deterministic verification + independent review
  ↓
immutable build
  ↓
candidate deployment
  ↓
offline evaluation
  ↓
canary
  ↓
promotion or rollback
  ↓
post-promotion soak
  ↓
ReleasedVersion
```

Autonomous Development owns:

```text
DevelopmentTarget
ProductObjectiveRevision
DevelopmentRequest
RequirementAnalysis
ChangeProposal
worktree and source semantics
verification gates
build artifact identity
deployment state
traffic exposure
feedback attribution
canary lifecycle
promotion
rollback
ReleasedVersion
```

The configured engineering executor performs bounded implementation work; Autonomous Development retains lifecycle and release authority.

World Runtime owns generic responsibility, authority, durable effect identity, and reality-effect admission.

Autonomous Development owns the meaning of a valid software release.

Git commit is not ReleasedVersion.

Tests passed is not promotion authority.

Deployment healthy is not ProductImproved.

Canary completion is not release finalization.

## Autonomous Development vertical slice

```text
Human
  ↓
Operator Interface
  ↓
IntentCandidate
  ↓
DevelopmentRequest
  ↓
Personal World
  ↓
purpose-limited context + basis revisions
  ↓
engineering executor requirement analysis
  ↓
RequirementAnalysis / ChangeProposal
  ↓
Autonomous Development lifecycle
  ↓
World Runtime
  ↓
governed reality-changing dispatch
  ↓
Git / build / deployment / traffic
  ↓
Reality
  ↓
tests / telemetry / deployment read-back / release evidence
  ↓
Autonomous Development
  ↓
domain outcome / ReleasedVersion / rollback / unknown
  ↓
World Runtime
  ↓
qualification / responsibility assessment / reconciliation
  ↓
Operator Interface
  ↓
human-facing projection
  ↓
Human
```

Personal World basis used by requirement analysis is revision-bound.

```text
Personal World record @ revision N
  ↓
RequirementAnalysis basis
  ↓
record changes / disappears / loses current qualification
  ↓
basis revalidation fails
  ↓
old analysis cannot silently continue
  ↓
revalidation / new analysis / human intervention
```

Personal context changes do not rewrite historical analysis.

Historical analysis does not imply current qualification.

## Reality return path

Every consequential path includes a return path.

```text
Reality
  ↓
observation / provider receipt / external state
  ↓
Domain evidence
  ↓
Effect realization / Outcome / Unknown
  ↓
World Runtime reconciliation and qualification
  ↓
Responsibility assessment
  ↓
human-facing projection
  ↓
Operator Interface
  ↓
Human
```

Provider acknowledgement alone cannot terminate the loop.

Transport ambiguity preserves uncertainty.

Independent authoritative read-back resolves reality whenever the domain supports it.

Unknown remains a first-class state.

## Continuity model

The architecture carries three durable continuities.

```text
Personal continuity
  = Personal World

Agency continuity
  = World Runtime

Domain continuity
  = Domain Controllers
```

`semantic-language` preserves distinctions across all three.

Operator-facing projections are reconstructed from authoritative owners and are not a fourth durable authority store.

An Agent may be replaced without replacing any durable continuity.

An operator interface may be replaced without replacing Personal World, World Runtime, or Domain state.

A Domain Controller may evolve without moving its professional lifecycle into World Runtime.

World Runtime may restart without losing durable agency state.

## Authority path

```text
authenticated actor
  ↓
representation
  ↓
intent / proposal
  ↓
Decision
  ↓
Mandate / Authorization
  ↓
bounded Runtime transition authority
  ↓
domain-specific execution authorization
  ↓
durable effect identity
  ↓
provider dispatch
  ↓
reality
```

No earlier stage substitutes for a later stage.

Knowledge of a resource does not grant authority over the resource.

Representation of a principal does not automatically grant transition authority.

Transition authority does not automatically grant every reality effect.

Domain execution permission does not prove domain outcome.

## Evidence and qualification path

```text
Reality
  ↓
Observation
  ↓
Evidence
  ↓
Domain interpretation
  ↓
Outcome / Unknown candidate
  ↓
qualification
  ↓
Responsibility assessment
  ↓
current agency state
```

Evidence remains traceable to its source.

Historical evidence remains historical when current qualification changes.

Material basis changes trigger revalidation rather than silent continuation.

## Repository placement rules

A new cross-domain meaning belongs in `semantic-language` only when multiple domains require the same non-substitutable distinction.

A new durable cross-domain agency invariant belongs in `world-runtime`.

A new personal fact, preference, relationship, resource reference, or personal-context lineage belongs in `personal-world`.

A new professional lifecycle belongs in a Domain Controller.

A provider-specific implementation remains below its owning Domain Controller.

Operator interaction and projection logic belongs at the replaceable operator-interface boundary and must not become authoritative durable state.

Agent/executor logic remains replaceable and does not become a durable state owner by default.

Model routing and model transport remain replaceable integration concerns.

New components connect through explicit Runtime and Personal World boundaries rather than copying either substrate.

## Extension topology

Additional executors attach to the cognitive execution boundary.

```text
Agency / Domain request
  ↓
executor selection
  ├─ Agent adapter
  ├─ engineering executor
  └─ specialized executor
```

Additional Domain Controllers attach below World Runtime.

```text
World Runtime
  ├─ Control Plane
  ├─ Administrative
  ├─ Autonomous Development
  ├─ future domain
  └─ future domain
```

Additional providers attach below their owning domains.

```text
Domain Controller
  ├─ API
  ├─ application
  ├─ device
  ├─ infrastructure
  ├─ human
  └─ robot
```

New capability does not imply new Runtime semantics.

New model intelligence does not imply new durable authority.

New domain breadth does not imply a universal domain ontology.

## Stable architecture

```text
guide
    doctrine / qualification / distinctions
                     │
                     ▼
aios/semantic-language
    cross-domain semantic constitution

Human ⇄ Operator Interface
             │
             ├────────⇄ personal-world
             │               │
             │               ▼
             │        Agent / Executor
             │               │
             │               ▼
             └────────► domain admission
                             │
                             ▼
                       world-runtime
                             │
              ┌──────────────┼─────────────────┐
              ▼              ▼                 ▼
        control-plane   administrative   autonomous-development
              │              │                 │
              ▼              ▼                 ▼
           providers      providers          providers
              │              │                 │
              └──────────────┼─────────────────┘
                             ▼
                           Reality
                             │
                             └──── evidence / outcome / unknown ────►
                                   domains ─► runtime ─► operator ─► Human

Agent / Executor
  ↓
model provider / routing adapter
  ↓
model provider
```



```text
guide
    doctrine / qualification / distinctions
                     │
                     ▼
semantic-language
    cross-domain semantic constitution

Human ⇄ agency-console
             │
             ├────────⇄ personal-world
             │               │
             │               ▼
             │             Codex
             │               │
             │               ▼
             └────────► domain admission
                             │
                             ▼
                       world-runtime
                             │
              ┌──────────────┼─────────────────┐
              ▼              ▼                 ▼
        control-plane   administrative   autonomous-development
              │              │                 │
              ▼              ▼                 ▼
           providers      providers          providers
              │              │                 │
              └──────────────┼─────────────────┘
                             ▼
                           Reality
                             │
                             └──── evidence / outcome / unknown ────►
                                   domains ─► runtime ─► console ─► Human

Codex
  ↓
litellm-gateway
  ↓
model providers
```
