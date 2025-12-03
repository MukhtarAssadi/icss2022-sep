class PlayCheapCards: pass
class PlayCheapEntities: pass
class PlayTechnologies: pass
class PlayEntitiesFirst: pass
class SaveEnergy: pass
class SpendAllEnergy: pass
class ConditionalAction:
    def __init__(self, condition, action, else_action=None):
        self.condition = condition
        self.action = action
        self.else_action = else_action

# Attack actions
class AttackPlayer: pass
class AttackOpponentDirectly: pass
class AttackWeakestEntity: pass
class AttackLowestHpEntity: pass
class AttackHighestPowerEntity: pass
class AttackPlayerIfNoEntities: pass

# Existence-based actions
class PlayCareful: pass
class FinishOpponent: pass
class GoAllIn: pass

# Style actions
class AggressiveStyle: pass
class DefensiveStyle: pass
class CautiousStyle: pass

# Conditions
class OpponentLowExistence: pass
class OpponentExistenceBelow:
    def __init__(self, value): self.value = value
class YouExistenceBelow:
    def __init__(self, value): self.value = value
class YouHaveNoEntities: pass
class YourHandFull: pass
class OpponentManyEntities: pass
