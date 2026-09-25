# AIOS Architecture

## Long-running autonomous runtime

```text
Long-running, unattended loop:

┌────────────────────────────────────┐       bounded effects       ┌─────────┐
│ AIOS Runtime                       ├─────────────────────────────►│ Reality │
│ observe → qualify → decide         │◄─────────────────────────────┤         │
│ → authorize → act → verify         │ authoritative read-back /    └─────────┘
│ Personal World / Runtime / Domains │ evidence / outcomes / unknowns
│ replaceable internal Agent/Executor│
└────────────────────────────────────┘
```

AIOS is a long-running AI runtime, designed for unattended operation with low
visibility. Its primary loop is AIOS acting on reality and incorporating
authoritative observations, read-back, and outcome evidence. Routine operation
does not depend on a person being present.

## Temporary external intervention

```text
Human
  │ query / request / approval when needed
  ▼
Existing Agent product
(short-lived client session)
  │ authoritative inspection / explanation / bounded authorized repair / verification
  ▼
AIOS integration boundary ─────────────► Reality, when an authorized effect is needed
  │
  └── report verified state to the Human, then disconnect
```

The user does not directly operate AIOS as an interactive assistant product.
When inspection, explanation, or maintenance is needed, the user may use an
existing Agent product as a temporary intervention adapter. The Agent reads
authoritative state, explains conditions, performs only bounded authorized
changes, verifies read-back and recovery, reports the result, and exits. AIOS
continues operating after the session ends.

This external Agent is not part of the AIOS runtime, is not a durable state or
authority owner, and is not a required runtime dependency. API/CLI boundaries
are machine integration and maintenance boundaries, not AIOS's primary human
management interface.

```text
Human presence != system operation
Human absence != suspended agency
Intervention session != durable agency
External Agent != AIOS authority owner
Agent explanation != authoritative state
Agent repair != successful recovery
Successful recovery = authoritative state + reality read-back + required verification
```

`semantic-language` supplies cross-domain semantic distinctions across the architecture.

`guide` holds doctrine, qualification rules, failure distinctions, and architectural invariants.

Agent implementations, model providers, model-routing gateways, monitoring systems, and deployment runtimes are replaceable integrations. None becomes a durable semantic owner merely because a deployment uses it.

## Architectural regions

```text
┌──────────────────────────────────────────────────────────────────────┐
│ AIOS — LONG-LIVED AUTONOMOUS RUNTIME                                 │
│                                                                      │
│ Personal World ──purpose-limited context───► internal Agent/Executor│
│       ▲                                     │                        │
│       │ provenance / revision                │ analysis / candidate  │
│       │                                     ▼                        │
│       └──────────────────────────► domain admission                  │
│                         │                                            │
│ semantic-language / World Runtime / Domain Controllers              │
│ responsibility / authority / work / effects / recovery / read-back   │
└─────────────────────────┬────────────────────────────────────────────┘
                          │ governed effect / evidence return
                          ▼
┌──────────────────────────────────────────────────────────────────────┐
│ REALITY                                                              │
│ external systems / source repositories / builds / deployments /      │
│ traffic / infrastructure / organizational systems                    │
└──────────────────────────────────────────────────────────────────────┘

OUT-OF-BAND, ONLY WHEN NEEDED
Human ⇄ existing short-lived Agent product ⇄ AIOS machine boundary
```

AIOS is headless and container-only at runtime. The containers are a
deployment boundary, not a durable semantic owner. Internal Agent/executor
implementations, model providers, monitoring systems, and external Agent
clients remain replaceable; none is required for the runtime's autonomous
continuity.

## Repository topology

| Repository / component | Ownership |
| --- | --- |
| [guide](https://github.com/xiongweilin/guide) | doctrine, qualification, distinctions, architectural invariants |
| [aios](https://github.com/xiongweilin/aios) | monorepo and Git owner for AIOS source components |
| [semantic-language](https://github.com/xiongweilin/aios/tree/main/src/semantic/semantic_language) | cross-domain meanings and non-substitution rules |
| [personal-world](https://github.com/xiongweilin/aios/tree/main/src/kernel/personal_world) | durable personal facts, preferences, relationships, resource links, provenance, revisions, freshness, privacy boundaries, purpose-limited context |
| [world-runtime](https://github.com/xiongweilin/aios/tree/main/src/kernel/world_runtime) | durable agency state, responsibility, authority, decisions, qualification, execution identity, recovery, reconciliation, history |
| [control-plane](https://github.com/xiongweilin/aios/tree/main/src/domains/control_plane) | operational incidents, bounded repair, monitoring, operational providers, operational outcome evidence |
| [administrative-orchestrator](https://github.com/xiongweilin/aios/tree/main/src/domains/administrative_orchestrator) | administrative cases, obligations, governance basis, administrative effects, business outcome and completion semantics |
| [autonomous-development](https://github.com/xiongweilin/aios/tree/main/src/domains/autonomous_development) | software-development lifecycle, requirements, source/build/test/deploy/canary/promotion/rollback semantics |
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

External Agent session state is ephemeral; it does not become durable authority, responsibility, or agency state.

## Temporary intervention boundary

Human intervention is out-of-band from the AIOS operating loop. When a query or
maintenance need arises, the user connects through an existing, replaceable
Agent product rather than directly operating AIOS.

```text
Human request / approval when needed
  ↓
short-lived external Agent session
  ↓
authenticated read of authoritative state
  ↓
explanation / diagnosis / bounded repair proposal
  ↓
explicit authorization when a state-changing action is required
  ↓
authoritative owner admission / effect
  ↓
reality read-back / recovery verification
  ↓
report to the Human, then disconnect
```

The external Agent owns only ephemeral session state and disposable
projections. It does not own durable authority, responsibility, Personal
World truth, domain lifecycle truth, domain outcomes, or runtime execution.

An API or CLI may serve as a machine integration or maintenance boundary. It
is not the primary human management interface and does not put the Human in the
long-term operating loop.

A command changes state only through the authoritative owner.

A projection remains read-only and disposable.

Ambiguous command transport remains `pending-reconciliation` until authoritative read-back resolves it. Ending an intervention session does not suspend or terminate AIOS agency.

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
autonomous domain trigger / standing mandate
  or
authorized request admitted through a temporary Agent session
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
qualified work trigger / authorized request
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
qualified development objective / admitted request
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
autonomous development trigger
  or
authorized request via temporary external Agent
  ↓
DevelopmentRequest admission
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
autonomous continuation / next work cycle
```

If a person needs an explanation or an intervention, an external Agent can
temporarily read the resulting authoritative state, carry out only an
authorized bounded repair, verify it, and exit. This is an exceptional access
path, not a required stage of the software lifecycle.

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
revalidation / new analysis / temporary external intervention if needed
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
current agency state / next autonomous cycle
```

Only when an exception requires human attention does a separate short-lived
Agent session project this state to the user.

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

External-Agent projections are reconstructed from authoritative owners and are not a fourth durable authority store.

An internal Agent/executor may be replaced without replacing any durable continuity.

A short-lived external Agent client may be replaced or disconnected without replacing Personal World, World Runtime, Domain state, or AIOS operation.

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

Short-lived external Agent interaction and projection logic remain outside AIOS; any AIOS API/CLI integration must not become an authoritative durable state owner.

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

AIOS — long-lived, headless runtime
    personal-world ──► internal Agent / Executor
           ▲                         │
           │                         ▼
           └────────────── domain admission
                                     │
                                     ▼
                               world-runtime
                                     │
                    ┌────────────────┼─────────────────┐
                    ▼                ▼                 ▼
              control-plane   administrative   autonomous-development
                    │                │                 │
                    ▼                ▼                 ▼
                 providers       providers          providers
                    │                │                 │
                    └────────────────┼─────────────────┘
                                     ▼ effects
                                  Reality
                                     │
                                     └── evidence / read-back / outcome / unknown
                                         ───────────────────────────────► AIOS

Out-of-band, only when needed:
Human ─► existing Agent product (short-lived session) ─► AIOS machine boundary
                 inspect / explain / bounded authorized repair / verify
                 ─► report ─► disconnect; AIOS continues

External Agent products, model providers, and routing adapters remain
replaceable integrations. The external intervention session is not a stage in
the continuous AIOS–Reality operating loop.
```
