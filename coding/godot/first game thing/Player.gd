extends Sprite

var speed = PI
var speed2 = 400.0

func _process(delta):
	var direction = 0
	
	if Input.is_action_pressed("ui_left"):
		direction = -1
	if Input.is_action_pressed("ui_right"):
		direction = 1
	
	var boost = 1
	
	rotation += PI * delta * direction
	
	if Input.is_action_pressed("ui_accept"):
		boost = 2
	
	var vel = Vector2.ZERO
	
	if Input.is_action_pressed("ui_up"):
		vel = Vector2.UP.rotated(rotation) * speed2 * boost
	
	position += vel * delta
